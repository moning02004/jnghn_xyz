from django.contrib.auth.models import User
from django.db import models


class FreeTalk(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    view = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title