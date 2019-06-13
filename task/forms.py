from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date"}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)

    class Meta:
        model = Task
        exclude = ("user",)

    def save(self, commit=True):
        """add user to task instance"""

        task = super().save(commit=False)
        task.user = self.request.user
        if commit:
            task.save()
        return task
