from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def request(angel):
     return HttpResponse('<h1><marquee> this view belong to angel </marquee></h1>')
