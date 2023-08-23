from django.contrib import admin
from list_app.models import Task_Model

# Register your models here.

class Task_ModelAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'discription','status')
    

admin.site.register(Task_Model,Task_ModelAdmin)