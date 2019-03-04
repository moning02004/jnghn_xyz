import os
from datetime import date
from django.db import models


def file_path(instance, filename):
    return 'me/{1}/Admin/{0}'.format(filename, date.today())


class Me(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    status = models.CharField(max_length=30)
    address = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class School(models.Model):
    me = models.ForeignKey(Me, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    period_from = models.DateField()
    period_to = models.DateField()
    graduate = models.TextField()

    def __str__(self):
        return self.name


class Army(models.Model):
    me = models.ForeignKey(Me, on_delete=models.CASCADE)
    graduate = models.TextField()
    period_from = models.DateField()
    period_to = models.DateField()
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.graduate


class Experience(models.Model):
    me = models.ForeignKey(Me, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class Attachment(models.Model):
    me = models.ForeignKey(Me, on_delete=models.CASCADE)
    file = models.FileField(upload_to=file_path, null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super(Attachment, self).delete(*args, **kwargs)

    def filename(self):
        return os.path.basename(self.file.name)

