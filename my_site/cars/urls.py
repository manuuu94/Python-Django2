from django.urls import path
from . import views


app_name = 'cars'

urlpatterns = [
    path('',views.Index,name='index'),
    path('list/',views.ListCar,name='list'),
    path('add/',views.AddCar,name='add'),
    path('delete/',views.DeleteCar,name='delete'),
    path('thankyou/',views.ThankYou,name='thankyou'),
    path('rentalreview/',views.RentalReview,name='rentalreview'),
    path('rentalreview2/',views.RentalReview2,name='rentalreview2'),

    ]






