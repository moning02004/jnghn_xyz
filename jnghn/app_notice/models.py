from django.db import models
from django.contrib.auth.models import User


class Notice(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
