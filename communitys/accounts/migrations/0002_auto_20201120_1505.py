# Generated by Django 3.1.3 on 2020-11-20 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='MBTI',
            field=models.CharField(choices=[(1, 'ESTJ'), (2, 'ESTP'), (3, 'ESFJ'), (4, 'ESFP'), (5, 'ENTJ'), (6, 'ENTP'), (7, 'ENFJ'), (8, 'ENFP'), (9, 'ISTJ'), (10, 'ISTP'), (11, 'ISFJ'), (12, 'ISFP'), (13, 'INTJ'), (14, 'INTP'), (15, 'INFJ'), (16, 'INFP')], max_length=50),
        ),
    ]