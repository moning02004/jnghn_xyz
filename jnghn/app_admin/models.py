import os
from datetime import date
from django.db import models


def file_path(instance, filename):
    return '{0}/{2}/Admin/{1}'.format(instance.archive.author.username, filename, date.today())


class Me(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    status = models.CharField(max_length=30)
    address = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Experience(models.Model):
    me = models.ForeignKey(Me, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.category


class Attachment(models.Model):
    archive = models.ForeignKey(Me, on_delete=models.CASCADE)
    file = models.FileField(upload_to=file_path, null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super(Attachment, self).delete(*args, **kwargs)

    def filename(self):
        return os.path.basename(self.file.name)

