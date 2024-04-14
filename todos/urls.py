from django.urls import path
from. import views

# This code defines URL patterns for a to-do list application using Django's path function.
# Each URL pattern maps a URL to a view function and gives it a name for reverse URL resolving.

urlpatterns = [
    # This URL pattern maps to the addTask view and gives it the name 'addTask'
    # The URL for this pattern is '/addTask/'
    path('addTask/', views.addTask, name='addTask'),

    # This URL pattern maps to the mark_as_done view and gives it the name 'mark_as_done'
    # The URL for this pattern is '/mark_as_done/<int:pk>/' where <int:pk> is the primary key of the task to be marked as done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),

    # This URL pattern maps to the mark_as_undone view and gives it the name 'mark_as_undone'
    # The URL for this pattern is '/mark_as_undone/<int:pk>' where <int:pk> is the primary key of the task to be marked as undone
    path('mark_as_undone/<int:pk>',views.mark_as_undone, name='mark_as_undone'),

    # This URL pattern maps to the edit_task view and gives it the name 'edit_task'
    # The URL for this pattern is '/edit_task/<int:pk>/' where <int:pk> is the primary key of the task to be edited
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),

    # This URL pattern maps to the delete_task view and gives it the name 'delete_task'
    # The URL for this pattern is '/delete_task/<int:pk>/' where <int:pk> is the primary key of the task to be deleted
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]