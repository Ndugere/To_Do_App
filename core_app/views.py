from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TaskForm
# Create your views here.



def tasks_view(request):
    tasks = request.session.get("tasks", [])
    return render(request, "core_app/index.html", {
        "all_tasks":tasks
    })

def add_a_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            tasks = request.session.get("tasks", [])
            tasks.append(task)
            request.session["tasks"] = tasks
            return HttpResponseRedirect(reverse("To_do_app:tasks_view"))
        else:
            return render(request, "core_app/add.html", {
                "form": form
            })
    return render(request, "core_app/add.html",
                  {
                      "form" : TaskForm()
                  })


def view_task(request, index):
    tasks = request.session.get("tasks", [])
    if 0<=index < len(tasks):
        task = tasks[index]
        return render(request, "core_app/detail_page.html", {"task":task})
    return HttpResponseRedirect(reverse("To_do_app:tasks_view"))


