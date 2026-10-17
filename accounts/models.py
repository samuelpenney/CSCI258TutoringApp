# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models 

class Subjects(models.TextChoices):
    CSCI = "CSCI", "Computer Science"
    MATH = "MATH", "Mathematics"
    ART = "ART", "Arts"
class CustomUser(AbstractUser): 
    age = models.PositiveIntegerField(null=True, blank=True)
    subject = models.CharField(choices=Subjects.choices, blank=True)