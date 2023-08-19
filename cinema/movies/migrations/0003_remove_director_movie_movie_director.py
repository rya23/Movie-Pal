# Generated by Django 4.2 on 2023-08-17 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "movies",
            "0002_remove_movie_actor_remove_movie_director_actor_movie_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="director",
            name="movie",
        ),
        migrations.AddField(
            model_name="movie",
            name="director",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                to="movies.director",
            ),
        ),
    ]
