from django.db import models
from django.template.defaultfilters import default, truncatechars
from django.utils.timezone import now

# Create your models here.
class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date = models.DateTimeField(default=now)
    body = models.TextField()
    img = models.ImageField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.name

    def snippet(self):
        return truncatechars(self.body, 200)

    def snippetTitle(self):
        return truncatechars(self.name, 34)

# Topic

# News Source