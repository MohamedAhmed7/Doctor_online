from django.urls import path
from .views import (index, ListUsers,
CreateUser, LoginUser, UpdateUser, DeleteUser)

urlpatterns = [
    path('', index),
    path('all', ListUsers.as_view()),
    path('register', CreateUser.as_view()),
    path('login', LoginUser.as_view()),
    path('update/<int:user_id>', UpdateUser.as_view()),
    path('delete/<int:user_id>', DeleteUser.as_view())

]
