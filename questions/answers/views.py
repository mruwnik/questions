from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404

from answers.models import Question, Category


def get_or_404(model, pk_id):
    try:
        return model.objects.get(pk=pk_id)
    except model.DoesNotExist:
        raise Http404('Invalid identifier provided')


def questions(request, search=None):
    """Get a list of all available questions."""
    questions = Question.objects
    if search:
        questions = questions.filter(content__icontains=search)

    return JsonResponse({'questions': list(questions.values())})


def categories(request, question, parent=None):
    """Get a list of categories for a given question/category pair."""
    get_or_404(Question, question)

    if parent:
        get_or_404(Category, parent)

    return JsonResponse({
        'question': question,
        'parent': parent,
        'categories': list(Category.objects.filter(question__id=question, parent__id=parent).values())
    })
