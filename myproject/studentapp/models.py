from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    enrollment = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    semester = models.IntegerField()

    def __str__(self):
        return self.name