from django.conf.urls import url
from .views import LanguageListView, LanguageDetailView
from .views import SnippetListView, SnippetDetailView
from .views import show_snippets_tree


urlpatterns = [
    url(r'^languages/$', LanguageListView.as_view()),
    url(r'^languages/(?P<pk>[0-9]+)/$', LanguageDetailView.as_view()),
    url(r'^snippets/$', SnippetListView.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetailView.as_view()),
    url(r'^snippets-tree-view/$', show_snippets_tree)
]