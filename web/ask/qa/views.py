from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET
from .shortcuts import render_question_list
from .models import Question
from .forms import AskForm, AnswerForm


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


def get_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        form.set_question(question)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    else:
        form = AnswerForm()
        form.set_question(question)
    return render(request, 'question_details.html', {
        'question': question,
        'answers': question.answer_set.all(),
        'form': form,
    })


def ask_question(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'question_ask.html', {
        'form': form,
    })
