from django.shortcuts import render_to_response
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions

from .models import Language, Snippet
from .serializers import LanguageSerializer, SnippetSerializer
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly

def show_snippets_tree(request):
    return render_to_response('oneide/snippets.html',
        {'snippets': Snippet.objects.all()})


class LanguageListView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class SnippetListView(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

