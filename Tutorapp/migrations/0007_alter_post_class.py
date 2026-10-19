from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Tutorapp", "0006_alter_post_ta"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="Class",
            field=models.CharField(
                choices=[
                    ("CSCI150", "CSCI150 - Introduction to Computer Science"),
                    ("CSCI151", "CSCI151 - Interdisciplinary I"),
                    ("CSCI232", "CSCI232 - Intermediate Data Structures & Alogrithms"),
                    ("ART101", "ART101 - Introduction to Art"),
                    ("MATH171", "MATH171 - Calculus 1"),
                ],
                max_length=200,
            ),
        ),
    ]
