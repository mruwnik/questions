from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404


from answers.models import Question, Category, Answer


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
    question = get_object_or_404(Question, pk=question_id)
    return format_categories(
        question, question.content,
        list(Category.objects.filter(question__id=question_id, parent__id=None).values('id', 'title'))
    )


def category(request, question_id, parent):
    """Get a list of categories for a given question/category pair."""
    question = get_object_or_404(Question, pk=question_id)
    category = get_object_or_404(Category, pk=parent)
    return format_categories(
        question, category.title, list(category.category_set.values('id', 'title')), category.parent_id,
        list(category.answers.values('id', 'title'))
    )


def answer(request, answer_id):
    """Get an answer."""
    answer = get_object_or_404(Answer, pk=answer_id)
    return JsonResponse({
        'id': answer_id,
        'title': answer.title,
        'answer': answer.content,
        'categories': list(answer.categories.values('id', 'title')),
        'sources': list(answer.sources.values()),
    })
