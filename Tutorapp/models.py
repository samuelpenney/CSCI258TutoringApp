from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Course(models.TextChoices):
    CSCI_151 = "CSCI151", "CSCI151 - Interdisciplinary I"
    CSCI_232 = "CSCI232", "CSCI232 - Intermediate Data Structures & Alogrithms"
    MATH_172 = "MATH172", "MATH172 - Calculus II"
    MATH_326 = "MATH326", "MATH326 - Introduction to Abstract Mathematics"
    MATH_273 = "MATH273", "MATH273 - Multivariable Calculus"
    ART_105A = "ART105A", "ART105A - Visual Language - Drawing"


class Post(models.Model):
    Class = models.CharField(max_length=200, choices=Course.choices)
    TA = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    Date = models.DateTimeField(default=timezone.now)
        
    def __str__(self):
        return self.Class

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})