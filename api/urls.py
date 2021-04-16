
from django.urls import path
from .views import index, userView, createUser, loginUser

urlpatterns = [
    path('', index),
    path('user/<int:user_id>', userView.as_view()),
    path('register', createUser.as_view()),
    path('login', loginUser.as_view())
]
