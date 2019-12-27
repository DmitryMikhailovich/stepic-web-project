from django import forms
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        return super().clean()

    def save(self):
        self.cleaned_data['author_id'] = 1 #zalepa
        return Question.objects.create(**self.cleaned_data)


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(queryset=None, empty_label=None)

    def __init__(self, question, *args, **kwargs):
        super().__init__(*args, **kwargs)
        queryset = Question.objects.filter(id=question.id)
        self.fields['question'].queryset = queryset

    def clean(self):
        return super().clean()

    def save(self):
        self.cleaned_data['author_id'] = 1  # zalepa
        return Answer.objects.create(**self.cleaned_data)
