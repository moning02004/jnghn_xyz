from django.db import models
from django.contrib.auth.models import User
from datetime import date
import os

from app_plan.models import Plan


def file_path(instance, filename):
    return '{0}/{2}/Review/{1}'.format(instance.review.author.username, filename, date.today())


class Review(models.Model):
    # index
    plan = models.ForeignKey(Plan, models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    view = models.PositiveIntegerField(default=0)

    content = models.TextField()
    def __str__(self):
        return self.title


class Image(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    image_file = models.ImageField(upload_to=file_path, null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.image_file.delete()
        super(Image, self).delete()

    def filename(self):
        return os.path.basename(self.image_file.name)


class Cost(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    cost_content = models.TextField(null=True)
    cost = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.cost_content


class HeartReview(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class CommentReview(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.user
