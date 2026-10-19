import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Tutorapp", "0008_remove_post_date_post_day_post_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="Date",
            field=models.DateField(default=django.utils.timezone.localdate),
        ),
    ]
