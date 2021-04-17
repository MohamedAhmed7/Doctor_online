
from django.urls import path
from .views import (index, ListClinics,
RetrieveClinic, CreateClinic, UpdateClinic, DeleteClinic)

urlpatterns = [
    path('', index),
    path('all', ListClinics.as_view()),
    path('create', CreateClinic.as_view()),
    path('<int:clinic_id>', RetrieveClinic.as_view()),
    path('update/<int:clinic_id>', UpdateClinic.as_view()),
    path('delete/<int:clinic_id>', DeleteClinic.as_view())

]
