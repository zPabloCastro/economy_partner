<<<<<<< HEAD
from django.http import HttpResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):
    return HttpResponse('API Documentation')
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> main
