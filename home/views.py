from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import UserAccountSerializer
from django.contrib.auth.models import User
from  . import models
# Create your views here.



def home(request):
    return render(request,'home/home.html')




@api_view(['GET'])
def raw_data(request):
    users = models.User_Account.objects.all()
    serializer = UserAccountSerializer(users, many=True)
    return Response(serializer.data)