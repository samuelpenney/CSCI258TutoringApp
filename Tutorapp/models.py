from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from accounts.models import Courses
# Create your models here.

class Post(models.Model):
    Class = models.CharField(max_length=200, choices=Courses.choices)
    TA = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    Date = models.DateTimeField(default=timezone.now)
        
    def __str__(self):
        return self.Class

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})