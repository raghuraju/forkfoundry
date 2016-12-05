from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Language(models.Model):
    name = models.CharField(max_length = 100)
    default_ext = models.CharField(max_length = 5)
    default_exec_ext = models.CharField(max_length = 5)
    default_compilation_command = models.CharField(max_length = 10, null = True, blank = True)
    default_run_command = models.CharField(max_length = 10)

    def __unicode__(self):
        return self.name.capitalize()


class Snippet(MPTTModel):
    title = models.CharField(max_length = 100)
    code = models.TextField()
    owner = models.ForeignKey(User, related_name='snippets', on_delete = models.DO_NOTHING)
    code = models.TextField()
    language = models.ForeignKey(Language, on_delete = models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    compilation_output = models.TextField(blank=True, null=True)
    execution_output = models.TextField(blank=True, null=True)
    successful = models.BooleanField(default = False)
    parent = TreeForeignKey('self', null = True, blank = True,
                related_name = 'forks', db_index = True)

    def __unicode__(self):
        return "{0}/{1}".format(self.owner.username, self.title)

