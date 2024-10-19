from django.contrib import admin
from . import models

class studentadmin(admin.ModelAdmin):
    list_display=('Student_name',)
admin.site.register(models.student,studentadmin)

class tutoradmin(admin.ModelAdmin):
    list_display=('tutorname',)
admin.site.register(models.tutor,tutoradmin)