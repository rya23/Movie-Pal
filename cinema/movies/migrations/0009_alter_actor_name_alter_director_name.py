# Generated by Django 4.2 on 2023-08-20 17:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0008_alter_movie_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actor",
            name="name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="director",
            name="name",
            field=models.CharField(max_length=50),
        ),
    ]
