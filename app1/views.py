from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bhavani(request):
    return HttpResponse('<h1><marquee>This view belongs to bhavani</h1><marquee>')
    