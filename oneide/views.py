from django.shortcuts import render_to_response
from rest_framework import generics

from .models import Language, Snippet
from .serializers import LanguageSerializer, SnippetSerializer


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


class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
