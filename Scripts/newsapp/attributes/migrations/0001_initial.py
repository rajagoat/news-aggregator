# Generated by Django 4.0 on 2021-12-17 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthNote',
            fields=[
                ('article_id', models.PositiveSmallIntegerField()),
                ('auth_note_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('article_id', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('user_id', models.PositiveSmallIntegerField()),
                ('note_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('about', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('article_id', models.PositiveSmallIntegerField()),
                ('rating_id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]