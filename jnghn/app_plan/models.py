from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Plan(models.Model):
    # index
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    created = models.DateTimeField(auto_now=True)
    view = models.PositiveIntegerField(default=0)
    where = models.CharField(max_length=100)
    password = models.CharField(max_length=100, default="", null=True)

    # detail
    day_from = models.DateField(null=False, blank=False, default=datetime.now)
    day_to = models.DateField(null=True)
    period = models.PositiveIntegerField(default=1)
    finish = models.CharField(max_length=100, default="No")

    def __str__(self):
        return self.title


class Days(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)


class Detail(models.Model):
    days = models.ForeignKey(Days, on_delete=models.CASCADE)
    major = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.major

    
class HeartPlan(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author


class CommentPlan(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.author
