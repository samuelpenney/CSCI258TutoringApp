import datetime
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from accounts.models import Courses

class Weekday(models.IntegerChoices):
    MONDAY = 0, "Monday"
    TUESDAY = 1, "Tuesday"
    WEDNESDAY = 2, "Wednesday"
    THURSDAY = 3, "Thursday"
    FRIDAY = 4, "Friday"
    SATURDAY = 5, "Saturday"
    SUNDAY = 6, "Sunday"

class Post(models.Model):
    Class = models.CharField(max_length=200, choices=Courses.choices)
    TA = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={"is_ta": True},
    )
    Date = models.DateField(default=timezone.localdate)
    Day = models.IntegerField(choices=Weekday.choices, editable=False)
    Time = models.TimeField(default=datetime.time(12, 0))
        
    def __str__(self):
        return self.Class

    def save(self, *args, **kwargs):
        if self.Date:
            self.Day = self.Date.weekday()
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})