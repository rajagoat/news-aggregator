# Generated by Django 4.0 on 2021-12-15 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_name',
            new_name='name',
        ),
    ]
