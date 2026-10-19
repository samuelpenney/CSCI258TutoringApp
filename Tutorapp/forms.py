from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["Class", "Date", "Day", "Time"]
        widgets = {
            "Date": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            "Day": forms.Select(),
            "Time": forms.TimeInput(attrs={"type": "time"}),
        }
