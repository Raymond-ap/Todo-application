from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title','description','completed']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control data-entry', 'placeholder': 'Create a new todo...'}),
            'description': forms.Textarea(attrs={'class': 'form-control text-area ', 'placeholder': 'Description...'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input text-muted',}),
        }
