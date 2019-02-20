from django.db import models
from django.contrib.auth.models import User
from datetime import date
import os


def file_path(instance, filename):
    return '{0}/{2}/Archive/{1}'.format(instance.archive.author.username, filename, date.today())


class Archive(models.Model):
    # index
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    view = models.PositiveIntegerField(default=0)

    # detail
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
 

class Attachment(models.Model):
    archive = models.ForeignKey(Archive, on_delete=models.CASCADE)
    file = models.FileField(upload_to=file_path, null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super(Attachment, self).delete(*args, **kwargs)

    def filename(self):
        return os.path.basename(self.file.name)


class CommentArchive(models.Model):
    archive = models.ForeignKey(Archive, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
