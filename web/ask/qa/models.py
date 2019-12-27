from django.db import models
from django.urls import reverse
import django.contrib.auth.models as contrib_models


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True)
    author = models.ForeignKey(to=contrib_models.User, on_delete=models.DO_NOTHING, related_name='question_author')
    likes = models.ManyToManyField(to=contrib_models.User, related_name='likes')
    objects = QuestionManager()

    def get_url(self):
        return reverse('qa:question', kwargs={'question_id': self.id})

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(to=Question, on_delete=models.DO_NOTHING, related_name='answer_set')
    author = models.ForeignKey(to=contrib_models.User, on_delete=models.DO_NOTHING, related_name='answer_author')

    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.__unicode__()
