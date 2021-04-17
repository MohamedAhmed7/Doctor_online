from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import CustomUser
from rest_framework.decorators import api_view
from .serializers import ClinicSerializer
from .models import Clinic

# Create your views here.

# api overvirew
# GET clinics
@api_view(['GET'])
def index(request):
    api_urls = {
		'List all clinics':'/clinics/all',
        'Retrieve clinic':'/clinics/clinic_id',
		'Update clinic':'/clinics/update/clinic_id',
		'Delete clinic':'/clinics/delete/clinic_id',
		}
    return Response(api_urls)

# @route  GET clinics/all
# @desc   List all clinics
# @access public
class ListClinics(generics.ListAPIView):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()

# @route  GET clinics/clinic_id
# @desc   Retrieve clinic
# @access public
class RetrieveClinic(generics.RetrieveAPIView):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()
    lookup_url_kwarg = "clinic_id"

# @route  POST clinics/create
# @desc   create new clinic
# @access public
class CreateClinic(generics.CreateAPIView):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()

# @route  PUT clinics/update/clinic_id
# @desc   update clinic
# @access public
class UpdateClinic(generics.UpdateAPIView):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()
    lookup_url_kwarg = "clinic_id"

# @route  Delete clinics/delete/clinic_id
# @desc   delete clinic
# @access public
class DeleteClinic(generics.DestroyAPIView):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()
    lookup_url_kwarg = "clinic_id"