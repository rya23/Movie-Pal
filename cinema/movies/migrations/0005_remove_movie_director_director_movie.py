# Generated by Django 4.2 on 2023-08-17 18:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0004_alter_movie_director"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="director",
        ),
        migrations.AddField(
            model_name="director",
            name="movie",
            field=models.ManyToManyField(
                blank=True, related_name="director", to="movies.movie"
            ),
        ),
    ]
