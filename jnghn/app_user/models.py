from django.contrib.auth.models import User
from django.db import models


class Friends(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend = models.CharField(max_length=50, null=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.friend
