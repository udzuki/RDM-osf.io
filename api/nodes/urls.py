from django.conf.urls import url

from api.nodes import views

app_name = 'osf'

urlpatterns = [
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.NodeList.as_view(), name=views.NodeList.view_name),
    url(r'^(?P<node_id>\w+)/$', views.NodeDetail.as_view(), name=views.NodeDetail.view_name),
    url(r'^(?P<node_id>\w+)/addons/$', views.NodeAddonList.as_view(), name=views.NodeAddonList.view_name),
    url(r'^(?P<node_id>\w+)/addons/(?P<provider>\w+)/$', views.NodeAddonDetail.as_view(), name=views.NodeAddonDetail.view_name),
    url(r'^(?P<node_id>\w+)/addons/(?P<provider>\w+)/folders/$', views.NodeAddonFolderList.as_view(), name=views.NodeAddonFolderList.view_name),
    url(r'^(?P<node_id>\w+)/children/$', views.NodeChildrenList.as_view(), name=views.NodeChildrenList.view_name),
    url(r'^(?P<node_id>\w+)/citation/$', views.NodeCitationDetail.as_view(), name=views.NodeCitationDetail.view_name),
    url(r'^(?P<node_id>\w+)/citation/(?P<style_id>[-\w]+)/$', views.NodeCitationStyleDetail.as_view(), name=views.NodeCitationStyleDetail.view_name),
    url(r'^(?P<node_id>\w+)/comments/$', views.NodeCommentsList.as_view(), name=views.NodeCommentsList.view_name),
    url(r'^(?P<node_id>\w+)/implicit_contributors/$', views.NodeImplicitContributorsList.as_view(), name=views.NodeImplicitContributorsList.view_name),
    url(r'^(?P<node_id>\w+)/contributors/$', views.NodeContributorsList.as_view(), name=views.NodeContributorsList.view_name),
    url(r'^(?P<node_id>\w+)/contributors/(?P<user_id>\w+)/$', views.NodeContributorDetail.as_view(), name=views.NodeContributorDetail.view_name),
    url(r'^(?P<node_id>\w+)/draft_registrations/$', views.NodeDraftRegistrationsList.as_view(), name=views.NodeDraftRegistrationsList.view_name),
    url(r'^(?P<node_id>\w+)/draft_registrations/(?P<draft_id>\w+)/$', views.NodeDraftRegistrationDetail.as_view(), name=views.NodeDraftRegistrationDetail.view_name),
    url(r'^(?P<node_id>\w+)/files/$', views.NodeProvidersList.as_view(), name=views.NodeProvidersList.view_name),
    url(r'^(?P<node_id>\w+)/files/providers/(?P<provider>\w+)/?$', views.NodeProviderDetail.as_view(), name=views.NodeProviderDetail.view_name),
    url(r'^(?P<node_id>\w+)/files/(?P<provider>\w+)(?P<path>/(?:.*/)?)$', views.NodeFilesList.as_view(), name=views.NodeFilesList.view_name),
    url(r'^(?P<node_id>\w+)/files/(?P<provider>\w+)(?P<path>/.+[^/])$', views.NodeFileDetail.as_view(), name=views.NodeFileDetail.view_name),
    url(r'^(?P<node_id>\w+)/forks/$', views.NodeForksList.as_view(), name=views.NodeForksList.view_name),
    url(r'^(?P<node_id>\w+)/identifiers/$', views.NodeIdentifierList.as_view(), name=views.NodeIdentifierList.view_name),
    url(r'^(?P<node_id>\w+)/institutions/$', views.NodeInstitutionsList.as_view(), name=views.NodeInstitutionsList.view_name),
    url(r'^(?P<node_id>\w+)/linked_nodes/$', views.LinkedNodesList.as_view(), name=views.LinkedNodesList.view_name),
    url(r'^(?P<node_id>\w+)/linked_registrations/$', views.NodeLinkedRegistrationsList.as_view(), name=views.NodeLinkedRegistrationsList.view_name),
    url(r'^(?P<node_id>\w+)/logs/$', views.NodeLogList.as_view(), name=views.NodeLogList.view_name),
    url(r'^(?P<node_id>\w+)/node_links/$', views.NodeLinksList.as_view(), name=views.NodeLinksList.view_name),
    url(r'^(?P<node_id>\w+)/node_links/(?P<node_link_id>\w+)/', views.NodeLinksDetail.as_view(), name=views.NodeLinksDetail.view_name),
    url(r'^(?P<node_id>\w+)/preprints/$', views.NodePreprintsList.as_view(), name=views.NodePreprintsList.view_name),
    url(r'^(?P<node_id>\w+)/registrations/$', views.NodeRegistrationsList.as_view(), name=views.NodeRegistrationsList.view_name),
    url(r'^(?P<node_id>\w+)/relationships/institutions/$', views.NodeInstitutionsRelationship.as_view(), name=views.NodeInstitutionsRelationship.view_name),
    url(r'^(?P<node_id>\w+)/relationships/linked_nodes/$', views.NodeLinkedNodesRelationship.as_view(), name=views.NodeLinkedNodesRelationship.view_name),
    url(r'^(?P<node_id>\w+)/relationships/linked_registrations/$', views.NodeLinkedRegistrationsRelationship.as_view(), name=views.NodeLinkedRegistrationsRelationship.view_name),
    url(r'^(?P<node_id>\w+)/view_only_links/$', views.NodeViewOnlyLinksList.as_view(), name=views.NodeViewOnlyLinksList.view_name),
    url(r'^(?P<node_id>\w+)/view_only_links/(?P<link_id>\w+)/$', views.NodeViewOnlyLinkDetail.as_view(), name=views.NodeViewOnlyLinkDetail.view_name),
    url(r'^(?P<node_id>\w+)/wikis/$', views.NodeWikiList.as_view(), name=views.NodeWikiList.view_name),
]
