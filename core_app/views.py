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
        return render(request, "core_app/detail_page.html", {"task":task, "index": index})
    return HttpResponseRedirect(reverse("To_do_app:tasks_view"))


def delete_task(request, index):
    tasks = request.session.get("tasks", [])
    if 0<=index<len(tasks):
        del tasks[index]
        request.session["tasks"] = tasks
        return HttpResponseRedirect(reverse("To_do_app:tasks_view"))


def update_task(request, index):
    tasks = request.session.get("tasks", [])
    if not (index >= 0 and index <len(tasks)):
        return HttpResponseRedirect(reverse("To_do_app:tasks_view"))
    
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            new_task = form.cleaned_data["task"]
            tasks[index] = new_task
            request.session['tasks'] = tasks
            return HttpResponseRedirect(reverse("To_do_app:tasks_view"))
        
        else:
            form = form
    
    else:
        current_task = tasks[index]
        form = TaskForm(initial={"task":current_task})

    return render(request, "core_app/update_task.html", {
        "form":form,
        "index": index
        })




