from rest_framework import serializers
from .models import Note, AuthNote, Comment, Rating

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['note_id', 'user_id', 'about']

class AuthNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthNote
        fields = ['id', 'lecture_title', 'course', 'due_date', 'lecture_number', 'content']

class  CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'course', 'due_date', 'assignment_number', 'content']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['student', 'assignment', 'grade_report', 'feedback', 'submission_time']