from django import forms
from .models import Todo

class PostForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("priority","title","content","due_date","success")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            'due_date': forms.SelectDateWidget

        }

