from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserSerializer, CreateUserSerializer#, #UserDetailSerializer
from django.http import Http404

class CustomUserList(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        #serializer = CreateUserSerializer(data=request.data)
        return Response(serializer.data)

    def post(self, request):
        #serializer = CustomUserSerializer(data=request.data)
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomUserDetail(APIView):
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = CustomUserSerializer(
        #UserDetailSerializer(
            instance=user,
            data=data,
            partial=True
        ) 
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                )
        return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
        )
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)