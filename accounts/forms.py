# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Courses
 
 
class CustomUserCreationForm(UserCreationForm): 
    courses = forms.MultipleChoiceField(
        choices=Courses.choices,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta: 
        model = CustomUser 
        fields = UserCreationForm.Meta.fields + ("courses",) 
 
 
class CustomUserChangeForm(UserChangeForm): 
    class Meta: 
        model = CustomUser 
        fields = UserChangeForm.Meta.fields
