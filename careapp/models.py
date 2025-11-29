from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    dob = models.DateField()
    email = models.EmailField()
    phone = models.IntegerField()
    visitdate = models.DateTimeField()
    medicalhistory = models.TextField()


    def __str__(self):
        return self.first_name


class MedicalRecords(models.Model):
    patientname = models.CharField(max_length=20)
    medicalhistory = models.TextField()
    diagnosis = models.CharField(max_length=20)


    def __str__(self):
        return self.patientname


class Appointment(models.Model):
    name =models.CharField(max_length=20)
    email =models.EmailField()
    phone =models.CharField(max_length=13)
    datetime =models.DateTimeField()
    department =models.CharField(max_length=50)
    doctor =models.CharField(max_length=50)
    message =models.TextField()



    def __str__(self):
        return self.name

























