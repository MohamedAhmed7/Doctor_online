from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from .serializers import userSerializer, userCreateSerializer
from users.models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response

def index(request):
    return HttpResponse('hello from api')

# @route  GET api/user/<int:user_id>
# @desc   retrieve or update or delete user
# @access public
class userView(generics.RetrieveUpdateAPIView):
    serializer_class = userSerializer
    queryset = CustomUser.objects.all()
    lookup_url_kwarg = 'user_id'

# @route  PosT api/register
# @desc   Create user
# @access public
class createUser(generics.CreateAPIView):
    serializer_class = userCreateSerializer
    queryset = CustomUser.objects.all()


# @route  PosT api/login
# @desc   login user
# @access public
class loginUser(APIView):
    serializer_class = userCreateSerializer

    def post(self, request):    
        try:
            username = request.data.get('username')
            password = request.data.get('password')
        except:
            return Response({'Bad Request':'Invalid Input'}, 
            status=status.HTTP_400_BAD_REQUEST)

        # check username or pass are empty
        if(len(username) == 0 or len(password) == 0):   
            return Response({'Bad Request':'Empty Input!'}, 
            status=status.HTTP_400_BAD_REQUEST)
        
        # check if user registerd or not 
        user_result = CustomUser.objects.filter(username = username)
        if (len(user_result) > 0):
            user = user_result[0]
            # check user password
            if(user.check_password(password)):
                return Response({'Success':'Login success!'}, 
                status=status.HTTP_200_ACCEPTED)
        else:
            return Response({'Bad Request':'User Not Found!'}, 
            status=status.HTTP_400_BAD_REQUEST)
        return Response({'Bad Request':'Error Bad Request'}, 
            status=status.HTTP_400_BAD_REQUEST)
