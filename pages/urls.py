from django.urls import path
from .views import Landing,About,Contact

urlpatterns = [
    path('',Landing.as_view(),name= 'landing'),
     path('contact/',Contact.as_view(),name= 'contact'),
    path('about/',About.as_view(),name= 'about')
]