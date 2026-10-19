from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_customuser_subjects_alter_customuser_is_ta"),
        ("accounts", "0009_alter_customuser_is_ta"),
    ]

    operations = [
        migrations.RemoveField(model_name="customuser", name="subjects"),
        migrations.AddField(
            model_name="customuser",
            name="subjects",
            field=models.JSONField(blank=True, default=list),
        ),
    ]
