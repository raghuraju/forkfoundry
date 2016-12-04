from django.conf.urls import url

from .views import api_root
from .views import LanguageListView, LanguageDetailView
from .views import SnippetListView, SnippetDetailView
from .views import UserListView, UserDetailView
from .views import show_snippets_tree


urlpatterns = [
    url(r'^$', api_root),
    url(r'^users/$', UserListView.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetailView.as_view(), name='user-detail'),
    url(r'^languages/$', LanguageListView.as_view(), name='language-list'),
    url(r'^languages/(?P<pk>[0-9]+)/$', LanguageDetailView.as_view(), name='language-detail'),
    url(r'^snippets/$', SnippetListView.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetailView.as_view(), name='snippet-detail'),
    url(r'^snippets-tree-view/$', show_snippets_tree)
]