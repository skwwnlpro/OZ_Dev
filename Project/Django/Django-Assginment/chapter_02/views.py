from django.shortcuts import render
from django.http import HttpResponse, Http404
from chapter_02.models import ToDo


# Create your views here.
def todo_list(request):
    todo_list = ToDo.objects.all()
    context = {"data": todo_list}

    return render(request, "todo_list.html", context)


def todo_info(request, todo_id):
    try:
        todo = ToDo.objects.get(pk=todo_id)
    except ToDo.DoesNotExist:
        raise Http404

    context = {"data": todo}
    return render(request, "todo_info.html", context)
