from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view ,APIView ,permission_classes
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import UserAccountSerializer,UserSession,UserContent
from django.contrib.auth.models import User
from  . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated

# Create your views here.



def home(request):
    return render(request,'home/home.html')


def upload_content(request):
    return render(request,'upload/upload.html')



@api_view(['GET'])
def raw_data(request):
    user_data = request.user

    user = models.User_Account.objects.get(id=user_data.id)
    serializer = UserAccountSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        serializer = UserSession(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data['name']
            password = serializer.validated_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None and user.is_authenticated:
                login(request,user)
                return Response({'message':'sucess'},status=status.HTTP_200_OK)

            else:
             return Response({'messsage':'wrong_creds'})

        else:
            return Response({'messsage':'error'})
        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Logout_user(request):
    if request.method == "GET":
        logout(request)
        return Response({'message':"sucess"},status=status.HTTP_200_OK)
        
    else:
        return Response({'message':'error'},status=status.HTTP_401_UNAUTHORIZED)
    


"""
{
  "post_title": "ajsdh",
  "content": "adasasd"
}


"""

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def User_content_upload(request):
    if request.method == "POST":
        serializer = UserContent(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message":'sucess'},status=status.HTTP_201_CREATED)
        else:
            return Response({"message":'error','errors':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def User_feed(request):
    contents = models.User_content.objects.all().order_by('-created')
    serializer = UserContent(contents,many=True)
    return Response(serializer.data)