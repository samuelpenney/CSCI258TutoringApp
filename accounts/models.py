# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models 

class Courses(models.TextChoices):
    CSCI_150 = "CSCI150", "CSCI150 - Introduction to Computer Science"
    CSCI_151 = "CSCI151", "CSCI151 - Interdisciplinary I"
    CSCI_232 = "CSCI232", "CSCI232 - Intermediate Data Structures & Alogrithms"

class CustomUser(AbstractUser): 
    courses = models.JSONField(default=list, blank=True)
    is_ta = models.BooleanField(default=True)

    def course_names(self):
        return [Courses(c).label for c in self.courses]