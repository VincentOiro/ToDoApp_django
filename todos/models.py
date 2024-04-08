from django.db import models

# This code defines a Django model class named 'Task' which represents a task in a to-do list application.
# Each task has a 'task' field to store the task description, an 'is_completed' field to track if the task is completed or not,
# and 'created_at' and 'updated_at' fields to store the timestamps of task creation and last update respectively.

class Task(models.Model):
    # The 'task' field is a character field with a maximum length of 250 characters to store the task description.
    task = models.CharField(max_length=250)

    # The 'is_completed' field is a boolean field to track if the task is completed or not. It defaults to False.
    is_completed = models.BooleanField(default=False)

    # The 'created_at' field is a DateTime field to store the timestamp of task creation. It is automatically set when a new task is created.
    created_at = models.DateTimeField(auto_now_add=True)

    # The 'updated_at' field is a DateTime field to store the timestamp of the last update to the task. It is automatically updated every time the task is updated.
    updated_at = models.DateTimeField(auto_now=True)

    # The '__str__' method is overridden to return the task description when a Task object is converted to a string.
    def  __str__(self):
        return self.task