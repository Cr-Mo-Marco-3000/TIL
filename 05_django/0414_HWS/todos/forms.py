from django import forms
from .models import Todo
from django.contrib.auth.forms import forms

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        exclude = ('author',)
