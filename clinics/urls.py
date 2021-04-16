
from django.urls import path
from .views import (index, ShowClinics,
                 update_or_delete_clinic, CreateClinic)

urlpatterns = [
    path('', index),
    path('all', ShowClinics.as_view()),
    path('<int:clinic_id>', update_or_delete_clinic.as_view()),
    path('create', CreateClinic.as_view())
]
