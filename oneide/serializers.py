from .models import Language, Snippet
from rest_framework import serializers


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = (
            'id',
            'name',
            'default_ext',
            'default_exec_ext',
            'default_compilation_command',
            'default_run_command',
        )


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = (
            'id',
            'title',
            'code',
            'owner',
            'language',
            'created',
            'modified',
            'output',
            'successful',
            'parent',
            'tree_id',
        )