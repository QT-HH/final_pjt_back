# Generated by Django 3.1.3 on 2020-11-25 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communitys', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='movie_title',
        ),
    ]
