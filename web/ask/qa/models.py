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
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    author = models.ForeignKey(to=contrib_models.User, on_delete=models.DO_NOTHING, related_name='question_author')
    likes = models.ManyToManyField(to=contrib_models.User, related_name='likes')
    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(to=Question, on_delete=models.DO_NOTHING, related_name='question_answer')
    author = models.ForeignKey(to=contrib_models.User, on_delete=models.DO_NOTHING, related_name='answer_author')
