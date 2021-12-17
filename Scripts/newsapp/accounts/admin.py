from django.contrib import admin
from .models import Profile, Reader


# # Register your models here.
# class ProfileAdmin(admin.ModelAdmin):
#     model = Profile
#     list_display = ('user', 'birth_date', 'address')
#
# class ReaderAdmin(admin.ModelAdmin):
#     model = Reader
#     list_display = ('user', 'number_of_articles_read')


admin.site.register(Profile)
admin.site.register(Reader)

#
# class InstructorAdmin(admin.ModelAdmin):
#     model = Instructor
#     list_display = ('user', 'start_date', 'office_number', 'office_phone_number')
#
# admin.site.register(Profile, ProfileAdmin)
# admin.site.register(Student, StudentAdmin)
# admin.site.register(Instructor, InstructorAdmin)