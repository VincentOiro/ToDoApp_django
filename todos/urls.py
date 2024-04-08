from django.urls import path
from . import views

urlpatterns = [
    # This URL pattern maps to the addTask view and gives it the name 'addTask'
    path('addTask/', views.addTask, name='addTask'),
    # This URL pattern maps to the mark_as_done view and gives it the name 'mark_as_done'
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    path('mark_as_undone/<int:pk>',views.mark_as_undone, name='mark_as_undone'),
]
