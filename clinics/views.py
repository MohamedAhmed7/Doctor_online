from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from users.models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ClinicSerializer
from .models import Clinic
# Create your views here.

def index(request):
    return HttpResponse('hello from clinics')

# @route  GET clinics/all
# @desc   List all clinics
# @access public
class ShowClinics(generics.ListAPIView):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()

class update_or_delete_clinic(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()
    lookup_url_kwarg = "clinic_id"

class CreateClinic(generics.CreateAPIView):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()