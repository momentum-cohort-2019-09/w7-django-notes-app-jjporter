from django import forms
from notey.models import NotesList
from django.forms import ModelForm

class NotesForm(forms.ModelForm):

  class Meta:
    model = NotesList
    fields = ['title', 'description']