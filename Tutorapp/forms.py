from django import forms
from django.utils import timezone

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

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("Date")
        start = cleaned_data.get("TimeStart")
        now = timezone.localtime()

        if date and date < now.date():
            self.add_error("Date", "Invalid Date. You cannot book a date in the past.")
        elif date and start and date == now.date() and start < now.time():
            self.add_error("TimeStart", "Invalid Start Time. You cannot book a start time in the past.")

        return cleaned_data