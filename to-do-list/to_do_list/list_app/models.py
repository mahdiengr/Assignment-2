from django.db import models
from list_app.views import add_task, edit_task
# Create your models here.

class Task_Model(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=50)
    discription=models.CharField(max_length=200)
    status=models.BooleanField(default=False)
    