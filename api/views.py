from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import userSerializer, userCreateSerializer
from users.models import CustomUser
# Create your views here.

def index(request):
    return HttpResponse('hello from api')

class userView(generics.RetrieveUpdateAPIView):
    serializer_class = userSerializer
    queryset = CustomUser.objects.all()
    lookup_url_kwarg = 'user_id'

class createUser(generics.CreateAPIView):
    serializer_class = userCreateSerializer
    queryset = CustomUser.objects.all()


