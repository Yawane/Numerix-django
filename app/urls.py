from django.urls import path

from app.views import project_detail

urlpatterns = [
    path('<str:slug>', project_detail, name="project"),
]
