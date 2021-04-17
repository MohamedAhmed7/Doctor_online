from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import userSerializer, userCreateSerializer, userLoginSerializer
from users.models import CustomUser
from django.contrib.auth.hashers import make_password


# api overvirew
# GET reservations
@api_view(['GET'])
def index(request):
    api_urls = {
		'List all users':'/users/all',
        'Retrieve user':'/users/user_id',
		'Update user':'/users/update/user_id',
		'Delete user':'/users/delete/user_id',
		}
    return Response(api_urls)

# @route  GET users/all
# @desc   List all users
# @access public
class ListUsers(generics.ListAPIView):
    serializer_class = userSerializer
    queryset = CustomUser.objects.all()

# @route  PosT users/register
# @desc   Create user
# @access public
class CreateUser(generics.CreateAPIView):
    serializer_class = userCreateSerializer
    queryset = CustomUser.objects.all()
    validate_password = make_password

# @route  PUT users/update/user_id
# @desc   Update user
# @access public
class UpdateUser(generics.UpdateAPIView):
    serializer_class = userCreateSerializer
    queryset = CustomUser.objects.all()
    lookup_url_kwarg = 'user_id'

# @route  Delete users/delete/user_id
# @desc   Delete user
# @access public
class DeleteUser(generics.DestroyAPIView):
    serializer_class = userCreateSerializer
    queryset = CustomUser.objects.all()
    lookup_url_kwarg = 'user_id'

# @route  PosT users/login
# @desc   login user
# @access public
class LoginUser(APIView):
    serializer_class = userLoginSerializer

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
            # we can return token here for authorization
            if(user.check_password(password)):
                return Response({'Success':'Login success!'}, 
                status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'Bad Request':'User Not Found!'}, 
            status=status.HTTP_400_BAD_REQUEST)
        return Response({'Bad Request':'Error Wrong password'}, 
            status=status.HTTP_400_BAD_REQUEST)
