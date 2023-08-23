from django import forms
from list_app.models import Task_Model


class Task_Form(forms.ModelForm):
    class Meta:
        model=Task_Model
        fields = ['id', 'title', 'discription','status']
        
        

