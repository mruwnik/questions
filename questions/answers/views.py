from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404

from answers.models import Question, Category, Answer


def questions(request):
    """Display a list of all available questions."""
    context = {
        'questions': Question.objects,
    }
    return render(request, 'answers/base.html', context)


def categories(request, question_id, category_id=None):
    """Display the selected categories for a given question."""
    context = {
        'questions': Question.objects,
        'selected': get_object_or_404(Question, pk=question_id),
        'categories': Category.objects.filter(question__id=question_id, parent__id=category_id),
        'parent': category_id and get_object_or_404(Category, pk=category_id, question__id=question_id)
    }
    return render(request, 'answers/items.html', context)


def answer(request, question_id, category_id, answer_id):
    """Display an answer."""
    context = {
        'questions': Question.objects,
        'selected': get_object_or_404(Question, pk=question_id),
        'category': get_object_or_404(Category, pk=category_id, question__id=question_id),
        'answer': get_object_or_404(Answer, pk=answer_id),
    }
    return render(request, 'answers/answer.html', context)
