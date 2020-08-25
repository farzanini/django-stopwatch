from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.TextField("Task Name")
    start_time = models.DateTimeField("Start Time")
    stop_time = models.DateTimeField("Stop Time")
    elapse_time = models.DateTimeField("Elapse Time")
    memo = models.TextField("Memo")
    assignee = models.ForeignKey("Person", on_delete=models.CASCADE)

    def task_elapse_time(self):
        self.elapse_time = self.stop_time - self.start_time

    def __str__(self):
        return f"{self.name} : Elapsed time {self.elapse_time}"


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField("Balance", default=0)
