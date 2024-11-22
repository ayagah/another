from django.db import models

# Create your models here.
class patient(models.Model):
    Last_name=models.CharField(max_length=50)
    Middle_name=models.CharField(max_length=50)
    First_name=models.CharField(max_length=50)
    Id_number=models.IntegerField()
    Phone_number=models.IntegerField()
    patient_number=models.IntegerField()
    Admission_date=models.DateTimeField(auto_now_add=True)
    Discharge=models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.First_name} {self.Middle_name} {self.Last_name}"
    
