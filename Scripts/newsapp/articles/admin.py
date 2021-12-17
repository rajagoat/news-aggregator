from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
admin.site.register(Article, ArticleAdmin)
    