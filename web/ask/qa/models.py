from django.db import models
import django.contrib.auth.models as contrib_models


class QuestionManager(models.Manager):
    def new(self):
        pass

    def popular(self):
        pass


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.ForeignKey(to=contrib_models.User, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(to=contrib_models.User)
    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(to=Question, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(to=contrib_models.User, on_delete=models.DO_NOTHING)
