from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["Class", "Date", "TimeStart", "TimeEnd"]
        widgets = {
            "Date": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            "TimeStart": forms.TimeInput(attrs={"type": "time"}),
            "TimeEnd": forms.TimeInput(attrs={"type": "time"}),
        }
