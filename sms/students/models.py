from django.db import models

# Create your models here.
class Student(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    
    student_image = models.ImageField(upload_to="student_images", null=True, blank=True)

class Attendance(models.Model):
       
    SUBJECT_CHOICES = (
        ("Math", "Math"),
        ("Science", "Science"),
        ("History", "History"),
        ("English", "English"),
        ("Art", "Art"),
    ) 
    STATUS_CHOICE = (
        ("Present", "Present"),
        ("Absent", "Absent"),
    )

    students = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)  
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)