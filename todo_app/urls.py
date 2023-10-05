from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('create/', views.create, name='create-task'),
    path('update/<int:id>/', views.update_task, name='update-task')
]