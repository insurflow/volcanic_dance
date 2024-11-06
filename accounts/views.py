from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Sample registration view
@api_view(['POST'])
def register(request):
    # Your logic to register a user
    # e.g., validate the data and create a user
    return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)

# Sample login view
@api_view(['POST'])
def login(request):
    # Your logic to authenticate a user and issue a token
    return Response({"message": "Login successful!"})

# Sample view to get user profile information
@api_view(['GET'])
def user_profile(request):
    # Logic to fetch user profile info
    return Response({"message": "User profile fetched successfully!"})
