from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = (
        "Class",
        "TA",
        "Date",
        "Day",
        "TimeStart",
        "TimeEnd"
    )


admin.site.register(Post, PostAdmin)