from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import TodoForm
from .models import Todo, Status


def todosPage(request):
    p_address = request.META['REMOTE_ADDR']

    status = Status.objects.all()

    form = TodoForm()

    completed = request.GET.get('completed')
    if completed:
        todos = Todo.objects.filter(status=True)
    else:
        todos = Todo.objects.all().order_by('-created')

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos')

    context = {
        'form': form,
        'todos': todos,
        'status': status
    }
    return render(request, 'todo/index.html', context)


def updateTOdo(request, slug):
    todo = Todo.objects.get(slug=slug)
    form = TodoForm(instance=todo)

    # update todo
    if request.method == 'POST' and 'Update Todo' in request.POST:
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos')

    return render(request, 'todo/detail.html', context={
        'form': form,
        "todo": todo
    })


def deleteTodo(request, slug):
    todo = Todo.objects.get(slug=slug)
    todo.delete()
    return redirect('todos')


def clearCompleted(request):
    todo = Todo.objects.filter(status=True)
    todo.delete()
    return redirect('todos')
