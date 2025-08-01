from django.shortcuts import render

# Create your views here.

all_tasks = ["far", "foo", "bars"]

def tasks_view(request):

    return render(request, "core_app/index.html", {
        "all_tasks":all_tasks
    })

def add_a_task(request):
    return render(request, "core_app/add.html")
