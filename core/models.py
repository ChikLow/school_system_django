from django.db import models

# Create your models here.


# Модель "Предмет"
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Модель "Вчитель"
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.subject.name})"

# Модель "Клас"
class Class(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Модель "Учень"
class Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.student_class.name})"
