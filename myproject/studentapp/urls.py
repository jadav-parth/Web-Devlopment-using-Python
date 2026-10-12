from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list_url'),
    path('add/', views.student_create, name='student_add_url'),
    path('update/<int:pk>/', views.student_update, name='student_update_url'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete_url'),
    path('api/students/', views.student_api_list, name='student_api_list'),
]