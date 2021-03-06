from django.contrib.auth.models import User
from django.db import models


class Jnghner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    friend = models.ManyToManyField('self')

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    source = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message


class Unread(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return self.message
