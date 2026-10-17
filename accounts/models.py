# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models 

class Subjects(models.TextChoices):
    CSCI = "Computer Science"
    MATH = "Mathematics"
    ART = "Arts"
class CustomUser(AbstractUser): 
    age = models.PositiveIntegerField(null=True, blank=True)
    course = models.CharField(choices=Subjects.choices, blank=True)