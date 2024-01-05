from django.urls import path

from .views import *

urlpatterns = [    
    path('create/', blog_create, name='blog_create'),
    path('<int:pk>/', blog_detail, name='blog_detail'),
    path('edit/<int:pk>', blog_edit, name='blog_edit'),
    path('delete/<int:pk>', blog_delete, name='blog_delete'),
]
