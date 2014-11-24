// Configuration options
var port = 7007;
var dbHost = 'localhost';
var dbPort = 27017;
var dbName = 'sharejstest';

// Library imports
var sharejs = require('share');
var livedb = require('livedb');
var Duplex = require('stream').Duplex;
var WebSocketServer = require('ws').Server;
var express = require('express');
var http = require('http');

// Server setup
var mongo = require('livedb-mongo')(
    'mongodb://' + dbHost + ':' + dbPort + '/' + dbName,
    {safe:true}
);
var backend = livedb.client(mongo);
var share = sharejs.server.createClient({backend: backend});
var app = express();
var server = http.createServer(app);
var wss = new WebSocketServer({ server: server});

// Local variables
var docs = {};
var locked = {};

// Allow CORS
app.all('*', function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

// Serve static sharejs files
app.use(express.static(sharejs.scriptsDir));

// TODO: Can we access the relevant list without iterating over every client?
wss.broadcast = function(docId, message) {
    for (var i in this.clients) {
        var c = this.clients[i];
        if (c.userMeta && c.userMeta.docId === docId) {
            c.send(message);
        }
    }
};

wss.on('connection', function(client) {

    var stream = new Duplex({objectMode: true});

    stream._read = function() {};
    stream._write = function(chunk, encoding, callback) {
        if (client.state !== 'closed') {
            client.send(JSON.stringify(chunk));
        }
        callback();
    };

    stream.headers = client.upgradeReq.headers;
    stream.remoteAddress = client.upgradeReq.connection.remoteAddress;

    client.on('message', function(data) {

        if (client.userMeta && locked[client.userMeta.docId]) {
            console.log(client.userMeta.docId, 'is locked! No edits.');
            // TODO: Is this the best way to let the user know they can't edit?
            wss.broadcast(client.userMeta.docId, JSON.stringify({type: 'lock'}));
            return;
        }

        // Handle our custom messages separately
        data = JSON.parse(data);
        if (data.registration) {
            var docId = data.docId;
            var userId = data.userId;

            // Create a metadata entry for this document
            if (!docs[docId])
                docs[docId] = {};

            // Add user to metadata
            if (!docs[docId][userId]) {
                docs[docId][userId] = {
                    name: data.userName,
                    url: data.userUrl,
                    count: 1,
                    gravatar: data.userGravatar
                };
            } else {
                docs[docId][userId].count++;
            }

            // Attach metadata to the client object
            client.userMeta = data;

            console.log('new user:', data.userName, '| Total:', wss.clients.length);
            wss.broadcast(docId, JSON.stringify({type: 'meta', users: docs[docId]}));

            // Lock client if doc is locked
            if (locked[docId]) {
                client.send(JSON.stringify({type: 'lock'}));
            }
        } else {
            stream.push(data);
        }
    });

    client.on('close', function(reason) {
        if (client.userMeta) {
            var docId = client.userMeta.docId;
            var userId = client.userMeta.userId;

            if (docs[docId] && docs[docId][userId]) {
                docs[docId][userId].count--;
                if (docs[docId][userId].count === 0) {
                    if (!Object.keys(docs[docId]).length) {
                        delete docs[docId];
                    }
                }
            }

            console.log('rem user:', client.userMeta.userName, '| Total:', wss.clients.length);
            wss.broadcast(docId, JSON.stringify({type: 'meta', users: docs[docId]}));
        }

        stream.push(null);
        stream.emit('close');
    });

    stream.on('error', function(msg) {
       client.close(msg);
    });

    stream.on('end', function() {
        client.close();
    });

    // Give the stream to sharejs
    return share.listen(stream);

});

// Get list of docs/users as JSON
app.get('/users', function getUsers(req, res, next) {
    res.send(docs);
});

// TODO: Lock urls are only get requests for debug purposes. Change to post

// Lock a document
app.get('/lock/:id', function lockDoc(req, res, next) {
    locked[req.params.id] = true;
    wss.broadcast(req.params.id, JSON.stringify({type: 'lock'}));
    console.log(req.params.id + " was locked.");
    res.send(req.params.id + " was locked.");
});

// Lock a document
app.get('/unlock/:id', function lockDoc(req, res, next) {
    delete locked[req.params.id];
    wss.broadcast(req.params.id, JSON.stringify({type: 'unlock'}));
    console.log(req.params.id + " was unlocked.");
    res.send(req.params.id + " was unlocked.");
});

server.listen(port, function() {
    console.log('Server running at http://127.0.0.1:' + port);
});