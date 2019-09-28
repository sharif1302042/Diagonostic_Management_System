from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class UserCreate(APIView):
    def get(self,request):
        return Response("User Created Succesfully", status=status.HTTP_201_CREATED)