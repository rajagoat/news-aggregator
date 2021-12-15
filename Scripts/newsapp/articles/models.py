from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    no_of_pages = models.IntegerField()
    body = models.TextField()

    def __str__(self):
        return self.name

# Topic

# News Source