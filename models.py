from django.db import models

# Create your models here.

class Exam(models.Model):
    # course=models.Foreignkey(course,on_delete=models.CASCADE)
    question=models.CharField(max_length=100)
    
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    corrans=models.CharField(max_length=100)

    


class registration(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)




