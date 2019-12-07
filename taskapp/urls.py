from django.urls import path
from . import views

urlpatterns = [
    path('', views.addtask, name='addtask'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('mark_as_done/<list_id>', views.mark_as_done, name='mark_as_done')
]