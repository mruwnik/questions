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


def format_categories(question, title, sub_cats, parent_id=None, answers=None):
    return JsonResponse({
        'question': question.id,
        'title': title,
        'parent': parent_id,
        'categories': sub_cats,
        'answers': answers or [],
    })


def categories(request, question_id):
    """Get a list of categories for a given question."""
    question = get_or_404(Question, question_id)
    return format_categories(
        question, question.content,
        list(Category.objects.filter(question__id=question_id, parent__id=None).values('id', 'title'))
    )


def category(request, question_id, parent):
    """Get a list of categories for a given question/category pair."""
    question = get_or_404(Question, question_id)
    category = get_or_404(Category, parent)
    return format_categories(
        question, category.title, list(category.category_set.values('id', 'title')), category.parent_id,
        list(category.answers.values())
    )
