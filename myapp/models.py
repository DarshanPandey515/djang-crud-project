from django.db import models

# Create your models here.
STUDENT_CLASS_CHOICE = [
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
    (9,9),
    (10,10),
    (11,11),
    (12,12),
]

STUDENT_SECTION_CHOICE = [
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D'),
]

STUDENT_SEX_CHOICE = [
    ('Others','Others'),
    ('Male','Male'),
    ('Female','Female'),  
]


class Student(models.Model):
    Student_ID = models.AutoField(primary_key=True)
    Student_Name = models.CharField(max_length=100)
    Student_Class = models.IntegerField(choices=STUDENT_CLASS_CHOICE)
    Student_Age = models.IntegerField()
    Student_Section = models.CharField(max_length=20,choices=STUDENT_SECTION_CHOICE)
    Student_Sex = models.CharField(max_length=20,choices=STUDENT_SEX_CHOICE)

