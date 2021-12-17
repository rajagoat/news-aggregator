from rest_framework import serializers
from articles.models import Article, Topic, NewsSource

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['name']

class NewsSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsSource
        fields = ['name']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'name', 'date', 'body', 'img', 'slug', 'topic', 'newsSource']