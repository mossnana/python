from django.urls import path
from . import views

urlpatterns = [
    path('', views.template_render),
    path('<int:pk>/edit/', views.task_edit),
    path('<int:pk>/delete/', views.task_delete)
]