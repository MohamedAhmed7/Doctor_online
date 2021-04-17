from django.urls import path
from .views import (index, CreateReservation, 
ListReservations, UpdateReservation, DeleteReservation, RetrieveReservation)


urlpatterns =  [
    path('', index),
    path('create', CreateReservation.as_view()),
    path('all', ListReservations.as_view()),
    path('<int:res_id>', RetrieveReservation.as_view()), # get method
    path('update/<int:res_id>', UpdateReservation.as_view()), # put method
    path('delete/<int:res_id>', DeleteReservation.as_view()) # delete method

]