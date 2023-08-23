from django.shortcuts import render, redirect
from list_app.forms import Task_Form
from list_app.models import Task_Model
# Create your views here.



def home(request):
    return render(request, 'add_task.html')


def add_task(request):
    if request.method == 'POST':
        task = Task_Form(request.POST)
        if task.is_valid():
            print(task.cleaned_data)
            task.save()
            return redirect('show_task')
    else:
        task = Task_Form()

    return render(request, 'add_task.html', {'form': task})




def show_task(request):
    task = Task_Model.objects.all()
    print(task)
    return render(request, 'show_tasks.html', {'data': task})


def edit_task(request, id):
    taskmodel = Task_Model.objects.get(pk=id)
    taskform = Task_Form(instance=taskmodel)
    if request.method == 'POST':
        taskform = Task_Form(request.POST, instance=taskmodel)
        if taskform.is_valid():
            taskform.save()
            return redirect('show_task')
    return render(request, 'add_task.html', {'form': taskform})


def delete_book(request, id):
    taskmodel = Task_Model.objects.get(pk=id).delete()
    return redirect('show_task')
    
    
def complete_task(request, id):
    taskmodel = Task_Model.objects.get(pk=id)
    taskmodel.status = True
    taskmodel.save()
    return redirect('show_task')