from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import render

from .serializers import NoteSerializer, AuthNoteSerializer, CommentSerializer, RatingSerializer
from .models import Note, Comment, Rating, AuthNote


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse



# Create your views here.
# def authNotes(request):
#     return HttpResponse('authNotes')


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def authNotes(request):
    if request.method == 'GET':
        notes = AuthNote.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AuthNoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        notes = AuthNote.objects.get(pk=request.GET.get("auth_note_id"))
        notes.delete()
        return Response("DELETED")
    
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def notes(request):
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# def notes(request):
#     try:
#         notes = Note.objects.all()
#     except Note.DoesNotExist:
#         raise Http404("Notes does not exist")
#     return render(request, 'notes.html', {'notes': notes})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def comments(request):
    if request.method == 'GET':
        notes = Comment.objects.all()
        serializer = CommentSerializer(notes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def comments(request):
#     return HttpResponse('comments')

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def ratings(request):
    if request.method == 'GET':
        notes = Rating.objects.all()
        serializer = RatingSerializer(notes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def ratings(request):
#     return HttpResponse('ratings')