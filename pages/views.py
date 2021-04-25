from django.shortcuts import render
from django.views.generic import TemplateView

class Landing(TemplateView) :
    template_name  = 'landing.html'


class Contact(TemplateView) :
    template_name  = 'contact.html'      

class About(TemplateView) :
    template_name  = 'about.html'    

