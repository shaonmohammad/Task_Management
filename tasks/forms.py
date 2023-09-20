from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'border rounded w-full py-2 px-3',
            'placeholder': 'Enter task title',
        })

        self.fields['description'].widget.attrs.update({
            'class': 'border rounded w-full py-2 px-3',
            'placeholder': 'Enter task description',
        })

        self.fields['deadline'].widget = forms.DateInput(attrs={
            'class': 'border rounded w-full py-2 px-3',
            'placeholder': 'Select a date',
            'type': 'date',
        })
