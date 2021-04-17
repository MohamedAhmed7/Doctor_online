from django.db import models
from clinics.models import Clinic
from users.models import CustomUser
from datetime import datetime
# Create your models here.
class Reservations(models.Model):
    clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    patient_name = models.CharField(null=False, max_length=50)
    doctor_name = models.CharField(null=False, max_length=50)
    date = models.DateField(null=False)
    start_time = models.TimeField(null=False)

    def __str__(self):
        return self.patient_name + self.clinic_id