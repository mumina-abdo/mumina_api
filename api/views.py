from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from users.models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
import logging

# mumima
from django.shortcuts import render

def home(request):
    return render(request, 'home.html') 

def register_user(request):
    return render(request, 'register_user.html')  

# mumina


logger = logging.getLogger(__name__)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            logger.info(f'User registered successfully: {user.email}')
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        
        logger.error(f'User registration failed: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email or not password:
            return Response({'error': _('Email and password are required')}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            logger.info(f'Login attempt for non-existent user: {email}')
            return Response({'error': _('User does not exist')}, status=status.HTTP_404_NOT_FOUND)
        
        django_user = authenticate(username=email, password=password)
        if django_user:
            logger.info(f'User logged in successfully: {email}')
            return Response({}, status=status.HTTP_200_OK)
        
        logger.error(f'Login failed for user: {email}')
        return Response({'error': _('Invalid credentials')}, status=status.HTTP_401_UNAUTHORIZED)