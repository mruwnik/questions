from django.db import models


class Question(models.Model):
    """The question being asked - short and simple."""

    content = models.CharField(max_length=140)  # coz why be longer than a tweet

    def __str__(self):
        return self.content


class Category(models.Model):
    """A category of answers."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=140)

    @property
    def path(self):
        """Return the printable path to this category."""
        current = []
        parent = self.parent
        while parent and parent.title:
            current.append(parent.title)
            parent = parent.parent

        return self.question.content + ': ' + ' -> '.join(current)

    def __str__(self):
        return '%s (%s)' % (self.title, self.path)


class Answer(models.Model):
    """An answer,"""

    title = models.CharField(max_length=511)
    content = models.TextField()
    categories = models.ManyToManyField(Category, related_name='answers')

    def __str__(self):
        return self.title


class Source(models.Model):
    """Sources whence an answer came from."""

    name = models.CharField(max_length=255)
    url = models.CharField(max_length=2047)
    answers = models.ManyToManyField(Answer, related_name='sources')

    def __str__(self):
        return self.name
