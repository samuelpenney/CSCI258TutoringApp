# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models 

class Subjects(models.TextChoices):
    MATH = "MATH", "Mathematics"
    ART = "ART", "Arts"
    CSCI = "CSCI", "Computer Science"
    CHEM = "CHEM", "Chemistry"
    BIOL = "BIOL", "Biology"
    ENGL = "ENGL", "English"
    HIST = "HIST", "History"
    ECON = "ECON", "Economics"
    PSYC = "PSYC", "Psychology"

class Courses(models.TextChoices):
    CSCI_150 = "CSCI150", "CSCI150 - Introduction to Computer Science"
    CSCI_151 = "CSCI151", "CSCI151 - Interdisciplinary I"
    CSCI_232 = "CSCI232", "CSCI232 - Intermediate Data Structures & Algorithms"
    CSCI_323 = "CSCI323", "CSCI323 - Software Engineering"
    CSCI_258 = "CSCI258", "CSCI258 - Web Application Development"
    ART_101 = "ART101", "ART101 - Introduction to Art"
    ART_201 = "ART201", "ART201 - Drawing"
    MATH_171 = "MATH171", "MATH171 - Calculus 1"
    MATH_172 = "MATH172", "MATH172 - Calculus 2"
    MATH_220 = "MATH220", "MATH220 - Linear Algebra"
    CHEM_101 = "CHEM101", "CHEM101 - General Chemistry 1"
    BIOL_101 = "BIOL101", "BIOL101 - Introduction to Biology"
    ENGL_101 = "ENGL101", "ENGL101 - Writing 101"
    HIST_101 = "HIST101", "HIST101 - World History"
    ECON_101 = "ECON101", "ECON101 - Principles of Microeconomics"
    PSYC_101 = "PSYC101", "PSYC101 - Introduction to Psychology"

class CustomUser(AbstractUser): 
    courses = models.JSONField(default=list, blank=True)
    subjects = models.JSONField(default=list, blank=True)
    is_ta = models.BooleanField(default=True)

    def subject_names(self):
        return [Subjects(s).label for s in self.subjects]

    def course_names(self):
        return [Courses(c).label for c in self.courses]