from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()

    def save(self):
        self.cleaned_data['author'] = self._user
        return Question.objects.create(**self.cleaned_data)


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(queryset=None, empty_label=None)

    def set_question(self, question):
        queryset = Question.objects.filter(id=question.id)
        self.fields['question'].queryset = queryset

    def clean(self):
        cleaned_data = super().clean()

    def save(self):
        self.cleaned_data['author'] = self._user
        return Answer.objects.create(**self.cleaned_data)


class UserSignupForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

    def save(self):
        return User.objects.create_user(**self.cleaned_data)


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
        if user is None:
            raise forms.ValidationError('Wrong username or password!')
        return cleaned_data
