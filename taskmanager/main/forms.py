# Create your buttons here.
from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        #  class is a bootstrap style 
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a tasks name'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a tasks description'
            }),
        }
