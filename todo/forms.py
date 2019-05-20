from django import forms
from .models import Todo
from django.utils import timezone

class PostForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("priority","title","content","due_date")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            'due_date': forms.DateInput(format="%Y-%m-%d",attrs={'placeholder':"ex)"+timezone.datetime.now().strftime('%Y-%m-%d')})

        }

