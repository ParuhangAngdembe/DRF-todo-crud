from django.urls import path
from . import views
urlpatterns = [
    path("", views.apiOverView, name="apioverview" ),
    path("tasklist/", views.taskList, name="task-list"),
    path("taskdetail/<str:pk>/", views.taskDetail, name="task-detail"),
    path("taskCreate/", views.taskCreate, name="task-create"),
    path("taskupdate/<str:pk>/", views.taskUpdate, name="task-update"),
    path("taskdelete/<str:pk>/", views.taskDelete, name="task-delete"),
]
