from django.contrib.auth.models import User
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
    owner = serializers.ReadOnlyField(source='owner.username')
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
            'compilation_output',
            'execution_output',
            'successful',
            'parent',
            'tree_id',
        )


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
