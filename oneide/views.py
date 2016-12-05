from django.shortcuts import render_to_response
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Language, Snippet
from .serializers import LanguageSerializer, SnippetSerializer
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly

def show_snippets_tree(request):
    return render_to_response('oneide/snippets.html',
        {'snippets': Snippet.objects.all()})


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'languages': reverse('language-list', request=request, format=format),
#         'snippets': reverse('snippet-list', request=request, format=format),
#     })


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

