from django.db import models

# Create your models here.
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_name = models.CharField(max_length=100)
    no_of_pages = models.IntegerField()
    body = models.TextField()