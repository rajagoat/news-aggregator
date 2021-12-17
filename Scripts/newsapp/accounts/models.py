from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number_of_articles_read = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return f' {self.user.username} Reader'

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    awards = models.CharField(max_length=255)
    preferred_genre = models.CharField(max_length=255)

    def __str__(self):
        return f' {self.user.username} Reader'

# class Student(models.Model):
#     GRADE_TEN = '10'
#     GRADE_ELEVEN = '11'
#     GRADE_TWELVE = '12'
#     YEAR_CHOICES = [
#         (GRADE_TEN, '10th Grade'),
#         (GRADE_ELEVEN, '11th Grade'),
#         (GRADE_TWELVE, '12th Grade')
#     ]
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     year = models.CharField(max_length=2, choices=YEAR_CHOICES)
#     student_id_no = models.PositiveIntegerField(unique=True)
#
#     def __str__(self):
#         return f'{self.user.first_name} {self.user.last_name} ({self.student_id_no})'
