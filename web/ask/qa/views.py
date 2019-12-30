from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .shortcuts import render_question_list
from .models import Question
from .forms import AskForm, AnswerForm, UserSignupForm, UserLoginForm


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def return_404(request, *args, **kwargs):
    return HttpResponseNotFound('404')


def signup_new_user(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserSignupForm()
    return render(request, 'question_signup.html', {
        'form': form,
    })


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.clean())
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserLoginForm()
    return render(request, 'question_login.html', {
        'form': form,
    })


@require_GET
@login_required
def get_new(request):
    new_questions = Question.objects.new()
    return render_question_list(request, new_questions)


@require_GET
@login_required
def get_popular(request):
    popular_questions = Question.objects.popular()
    return render_question_list(request, popular_questions)


@login_required
def get_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        form.set_question(question)
        form._user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    else:
        form = AnswerForm()
        form.set_question(question)
        form._user = request.user
    return render(request, 'question_details.html', {
        'question': question,
        'answers': question.answer_set.all(),
        'form': form,
    })


@login_required
def ask_question(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
        form._user = request.user
    return render(request, 'question_ask.html', {
        'form': form,
    })
