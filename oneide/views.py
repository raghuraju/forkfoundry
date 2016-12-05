import os
import re
import uuid
import json
import subprocess

from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.conf import settings

from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Language, Snippet
from .serializers import LanguageSerializer, SnippetSerializer
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly, IsOwner

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

    @classmethod
    def extract_class_name(cls, code):
        class_name = re.findall(r'class (\w+)\s*{', code)
        # TODO: Throw an error if more than one class names were found
        return class_name[0]

    @detail_route(methods=['GET'])
    def fork(self, request, *args, **kwargs):
        snippet = self.get_object()
        scopy = Snippet(title = snippet.title,
            code = snippet.code,
            owner = request.user,
            compilation_output = snippet.compilation_output,
            execution_output = snippet.execution_output,
            language = snippet.language,
            parent = snippet)
        scopy.save()
        return Response(SnippetSerializer(scopy).data)


    @detail_route(permission_classes=[IsOwner])
    def run(self, request, *args, **kwargs):
        snippet = self.get_object()
        language = snippet.language

        if snippet.code:

            snippets_home = settings.SNIPPET_HOME
            snippet_home = os.path.join(snippets_home, str(snippet.id))

            if not os.path.exists(snippet_home):
                os.mkdir(snippet_home)
            os.chdir(snippet_home)

            if language.name.lower() == 'java':
                class_name = SnippetViewSet.extract_class_name(snippet.code)
            else:
                class_name = '_'.join([language.name.lower(), str(snippet.id)])

            file_name = '.'.join([class_name, language.default_ext])
            if language.default_exec_ext:
                exec_file_name = '.'.join([class_name, language.default_exec_ext])
            else:
                exec_file_name = class_name

            with open(os.path.join(snippet_home, file_name), 'w') as f:
                f.writelines(snippet.code)

            cmds = [language.default_compilation_command, language.default_run_command]
            
            # optional compilation phase
            if cmds[0]:
                proc = subprocess.Popen([cmds[0], file_name], stderr=subprocess.PIPE)
                std_err = proc.communicate()[1]
                if std_err:
                    snippet.compilation_output = std_err
                    snippet.successful = False
                    snippet.save()
                    return Response({'sucess': False, 'output': std_err, 'stage': 'compilation'})

            proc = subprocess.Popen([cmds[1], exec_file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            std_out, std_err = proc.communicate()
            if std_err:
                snippet.execution_output = std_err
                snippet.successful = False
                snippet.save()
                return Response({'sucess': False, 'output': std_err, 'stage': 'execution'})
            else:
                snippet.execution_output = std_out
                snippet.successful = True
                snippet.save()
                return Response({'sucess': True, 'output': std_out, 'stage': 'execution'})


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

