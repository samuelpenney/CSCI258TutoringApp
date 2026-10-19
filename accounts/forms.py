# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Courses, Subjects
 
 
class CustomUserCreationForm(UserCreationForm): 
    subjects = forms.MultipleChoiceField(
        choices=Subjects.choices,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    courses = forms.MultipleChoiceField(
        choices=Courses.choices,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta: 
        model = CustomUser 
        fields = UserCreationForm.Meta.fields + ("subjects", "courses")

    def clean(self):
        cleaned = super().clean()
        # Course codes start with their subject code, e.g. "CSCI150" belongs to "CSCI"
        subjects = cleaned.get("subjects", [])
        for course in cleaned.get("courses", []):
            if not any(course.startswith(s) for s in subjects):
                self.add_error("courses", "Choose only courses within your selected subjects.")
                break
        return cleaned
 
 
class CustomUserChangeForm(UserChangeForm): 
    class Meta: 
        model = CustomUser 
        fields = UserChangeForm.Meta.fields
