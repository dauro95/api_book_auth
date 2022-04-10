
# Create your views here.

from django.shortcuts import render

from rest_framework import viewsets

from .serializers import BookSerializer,AuthorSerializer
from .models import Author,Book

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])

def welcome(request,format=None):
    content = {"message": "Welcome to the BookStore!"}
    return JsonResponse(content)


class AuthorViewSet (viewsets.ModelViewSet):

    queryset=Author.objects.all()
    serializer_class=AuthorSerializer



class BookViewSet (viewsets.ModelViewSet):
    
    queryset=Book.objects.all()
    serializer_class=BookSerializer