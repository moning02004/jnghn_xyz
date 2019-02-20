from django.contrib.auth.models import User
from django.db import models


class Beans(models.Model):
    name = models.CharField(max_length=100)
    nation = models.CharField(max_length=100)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Account(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    purchase_site = models.CharField(max_length=100)
    begin_date = models.DateField(null=False)
    end_date = models.DateField(null=True)
    period = models.PositiveIntegerField(null=True)
    amount = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Community(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    view = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.author


class CommunityComment(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
