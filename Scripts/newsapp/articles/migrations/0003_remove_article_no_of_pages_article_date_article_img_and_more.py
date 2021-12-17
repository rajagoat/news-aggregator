# Generated by Django 4.0 on 2021-12-17 00:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_rename_article_id_article_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='no_of_pages',
        ),
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]