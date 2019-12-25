from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET
from .shortcuts import render_question_list
from .models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def return_404(request, *args, **kwargs):
    return HttpResponseNotFound('404')


@require_GET
def get_new(request):
    new_questions = Question.objects.new()
    return render_question_list(request, new_questions)


@require_GET
def get_popular(request):
    popular_questions = Question.objects.popular()
    return render_question_list(request, popular_questions)


@require_GET
def get_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'question_details.html', {
        'question': question,
        'answers': question.question_answer.all()
    })
