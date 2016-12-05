from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .views import LanguageViewSet
from .views import SnippetViewSet
from .views import UserViewSet
from .views import show_snippets_tree

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'languages', LanguageViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^snippets-tree-view/$', show_snippets_tree)
]