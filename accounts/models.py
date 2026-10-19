# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models 

class Subjects(models.TextChoices):
    MATH = "MATH", "Mathematic"
    ART = "ART", "Arts"
    CSCI = "CSCI", "Computer Science"

class Courses(models.TextChoices):
    CSCI_150 = "CSCI150", "CSCI150 - Introduction to Computer Science"
    CSCI_151 = "CSCI151", "CSCI151 - Interdisciplinary I"
    CSCI_232 = "CSCI232", "CSCI232 - Intermediate Data Structures & Alogrithms"
    ART_101 = "ART101", "ART101 - Introduction to Art"
    MATH_171 = "MATH171", "MATH171 - Calculus 1"

class CustomUser(AbstractUser): 
    courses = models.JSONField(default=list, blank=True)
    subjects = models.JSONField(default=list, blank=True)
    is_ta = models.BooleanField(default=True)

    def subject_names(self):
        return [Subjects(s).label for s in self.subjects]

    def course_names(self):
        return [Courses(c).label for c in self.courses]