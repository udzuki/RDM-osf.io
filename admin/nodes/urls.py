from django.conf.urls import url
from admin.nodes import views

app_name = 'admin'

urlpatterns = [
    url(r'^$', views.NodeFormView.as_view(),
        name='search'),
    url(r'^flagged_spam$', views.NodeFlaggedSpamList.as_view(),
        name='flagged-spam'),
    url(r'^known_spam$', views.NodeKnownSpamList.as_view(),
        name='known-spam'),
    url(r'^known_ham$', views.NodeKnownHamList.as_view(),
        name='known-ham'),
    url(r'^(?P<guid>[a-z0-9]+)/$', views.NodeView.as_view(),
        name='node'),
    url(r'^(?P<guid>[a-z0-9]+)/logs/$', views.AdminNodeLogView.as_view(),
        name='node-logs'),
    url(r'^registration_list/$', views.RegistrationListView.as_view(),
        name='registrations'),
    url(r'^(?P<guid>[a-z0-9]+)/update_embargo/$',
        views.RegistrationUpdateEmbargoView.as_view(), name='update_embargo'),
    url(r'^(?P<guid>[a-z0-9]+)/remove/$', views.NodeDeleteView.as_view(),
        name='remove'),
    url(r'^(?P<guid>[a-z0-9]+)/restore/$', views.NodeDeleteView.as_view(),
        name='restore'),
    url(r'^(?P<guid>[a-z0-9]+)/confirm_spam/$', views.NodeConfirmSpamView.as_view(),
        name='confirm-spam'),
    url(r'^(?P<guid>[a-z0-9]+)/confirm_ham/$', views.NodeConfirmHamView.as_view(),
        name='confirm-ham'),
    url(r'^(?P<guid>[a-z0-9]+)/reindex_share_node/$', views.NodeReindexShare.as_view(),
        name='reindex-share-node'),
    url(r'^(?P<guid>[a-z0-9]+)/reindex_elastic_node/$', views.NodeReindexElastic.as_view(),
        name='reindex-elastic-node'),
    url(r'^(?P<node_id>[a-z0-9]+)/remove_user/(?P<user_id>[a-z0-9]+)/$',
        views.NodeRemoveContributorView.as_view(), name='remove_user'),
]
