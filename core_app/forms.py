from django import forms

class TaskForm(forms.Form):
    task = forms.CharField(
        label="Enter Task",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g. Buy milk'
        })
    )
