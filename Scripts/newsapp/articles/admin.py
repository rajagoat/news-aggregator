from django.contrib import admin
from .models import Article, Topic, NewsSource

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
admin.site.register(Article, ArticleAdmin)

admin.site.register(Topic)
admin.site.register(NewsSource)