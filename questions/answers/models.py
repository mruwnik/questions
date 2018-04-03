from django.db import models


class Question(models.Model):
    """The question being asked - short and simple."""

    content = models.CharField(max_length=140)  # coz why be longer than a tweet


class Category(models.Model):
    """A category of answers."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=140)


class Answer(models.Model):
    """An answer,"""

    title = models.CharField(max_length=511)
    content = models.TextField()
    categories = models.ManyToManyField(Category, related_name='answers')


class Source(models.Model):
    """Sources whence an answer came from."""

    name = models.CharField(max_length=255)
    url = models.CharField(max_length=2047)
    answers = models.ManyToManyField(Answer, related_name='sources')
