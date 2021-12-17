from django.db import models
from django.template.defaultfilters import default, truncatechars
from django.utils.timezone import now

# Create your models here.
# Topic
class Topic(models.Model):
    name = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.name

# News Source
class NewsSource(models.Model):
    name = models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        return self.name

# Article
class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date = models.DateTimeField(default=now)
    body = models.TextField()
    img = models.ImageField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, max_length=50)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, default=None)
    newsSource = models.ForeignKey(NewsSource, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.name

    def snippet(self):
        return truncatechars(self.body, 200)

    def snippetTitle(self):
        return truncatechars(self.name, 34)