from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    roll_number = models.CharField(max_length=20)
    father_name = models.CharField(max_length=255)
    course = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)

    # Additional fields and methods can be added here as needed
    def __str__(self):
        return f"{self.name} {self.course}"
