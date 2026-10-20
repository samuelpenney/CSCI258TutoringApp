from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["Class", "Date", "Time"]
        widgets = {
            "Date": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            "Time": forms.TimeInput(attrs={"type": "time"}),
        }
