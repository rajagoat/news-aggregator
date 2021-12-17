from .serializers import NewsSourceSerializer, ArticleSerializer, TopicSerializer
from articles.models import NewsSource, Article, Topic

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        notes = Article.objects.get(pk=request.GET.get("auth_note_id"))
        notes.delete()
        return Response("DELETED")

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def topics(request):
    if request.method == 'GET':
        articles = Topic.objects.all()
        serializer = TopicSerializer(articles, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        notes = Topic.objects.get(pk=request.GET.get("auth_note_id"))
        notes.delete()
        return Response("DELETED")

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def newssource(request):
    if request.method == 'GET':
        articles = NewsSource.objects.all()
        serializer = NewsSourceSerializer(articles, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = NewsSourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        notes = NewsSource.objects.get(pk=request.GET.get("auth_note_id"))
        notes.delete()
        return Response("DELETED")