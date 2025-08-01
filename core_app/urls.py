from django.urls import path
from . import views

app_name = "To_do_app"

urlpatterns = [
    path("", views.tasks_view, name="tasks_view"),
    path("add/", views.add_a_task, name="add"),
    path("detail/<int:index>/", views.view_task, name="view_task"),
    path("delete_task/<int:index>/", views.delete_task, name="delete_task"),
]