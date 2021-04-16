from django.db import models
from users.models import CustomUser
# Create your models here.

class Clinic(models.Model):
    # one user(doctor) can hava more than one clinic
    # one to many relation
    user =  models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField(null=False, default=0.0)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)

    def __str__(self):
        return self.name