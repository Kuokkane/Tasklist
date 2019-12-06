from django.urls import path
from . import views

urlpatterns = [
    path('', views.addtask, name='addtask'),
    path('delete/<list_id>', views.delete, name='delete'),
]