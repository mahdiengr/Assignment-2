from django.urls import path
from list_app.views import home, add_task, show_task, edit_task, delete_book,complete_task

urlpatterns = [
    path('', home),
    path('add_task/', add_task, name='add_task'),
    path('show_task/', show_task, name='show_task'),
    path('edit_task/<int:id>', edit_task, name='edit_task'),
    path('delete_book/<int:id>', delete_book, name='delete_book'),
    path('complete_task/<int:id>', complete_task, name='complete_task'),
    

]
