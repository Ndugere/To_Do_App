from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

all_tasks = ["far", "foo", "bars"]

def tasks_view(request):

    return render(request, "core_app/index.html", {
        "all_tasks":all_tasks
    })

def add_a_task(request):
    if request.method == "POST":
        task = request.POST.get("task")
        if task:
            all_tasks.append(task)
            return HttpResponseRedirect(reverse("To_do_app:tasks_view"))
    return render(request, "core_app/add.html")
