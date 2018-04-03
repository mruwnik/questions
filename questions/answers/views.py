from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from answers.models import Question


def questions(request, search=None):
    """Get a list of all available questions."""
    questions = Question.objects
    if search:
        questions = questions.filter(content__icontains=search)

    return JsonResponse({'questions': list(questions.values())})
