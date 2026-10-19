import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Tutorapp", "0007_alter_post_class"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="Date"),
        migrations.AddField(
            model_name="post",
            name="Day",
            field=models.IntegerField(
                choices=[
                    (0, "Monday"),
                    (1, "Tuesday"),
                    (2, "Wednesday"),
                    (3, "Thursday"),
                    (4, "Friday"),
                    (5, "Saturday"),
                    (6, "Sunday"),
                ],
                default=0,
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="Time",
            field=models.TimeField(default=datetime.time(12, 0)),
        ),
    ]
