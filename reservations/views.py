from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Reservations
from .serializers import reservationSerializer
# Create your views here.

def index(request):
    return HttpResponse('hello from reservations')

# @route  POST reservations/create
# @desc   create new reservation
# @access public
class CreateReservation(generics.CreateAPIView):
    serializer_class = reservationSerializer
    queryset = Reservations.objects.all()

# @route  GET reservations/all
# @desc   List all reservations
# @access public
class ListReservations(generics.ListAPIView):
    serializer_class = reservationSerializer
    queryset = Reservations.objects.all()

# @route  PUT reservations/res_id
# @desc   update reservation
# @access public
class UpdateReservation(generics.UpdateAPIView):
    serializer_class = reservationSerializer
    queryset = Reservations.objects.all()
    lookup_url_kwarg = 'res_id'

# @route  Delete reservations/res_id
# @desc   delete reservation
# @access public
class DeleteReservation(generics.DestroyAPIView):
    serializer_class = reservationSerializer
    queryset = Reservations.objects.all()
    lookup_url_kwarg = 'res_id'

# @route  GET reservations/res_id
# @desc   retrive reservation
# @access public
class RetrieveReservation(generics.RetrieveAPIView):
    serializer_class = reservationSerializer
    queryset = Reservations.objects.all()
    lookup_url_kwarg = 'res_id'

