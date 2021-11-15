from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, ReadOnlyUserSerializer, WriteOnlyUserSerializer
from .models import ModelUser
from rest_framework import status
import json
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
import re


class UserList(generics.ListAPIView):
    queryset = ModelUser.objects.all()
    serializer_class = WriteOnlyUserSerializer
    permission_classes = [IsAuthenticated]

    @staticmethod
    @swagger_auto_schema(responses={201: ReadOnlyUserSerializer()})
    def post(self):
        try:
            load = json.loads(json.dumps(self.data))
            if re.fullmatch(r'^(?=.*[A-Z])(?=.*\d).{8,}$', load["password"]):
                new_user = ModelUser.objects.create(
                    username=load["username"],
                    first_name=load["first_name"],
                    last_name=load["last_name"],
                    password=load["password"],
                )
            else:
                return JsonResponse({"Пароль не подходит по требованиям":True})

            serializer = ReadOnlyUserSerializer(new_user)
            return JsonResponse({"users": serializer.data}, safe=False, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({"error": str(e)})


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ModelUser.objects.all()
    serializer_class = WriteOnlyUserSerializer

    @swagger_auto_schema(responses={200: ReadOnlyUserSerializer()})
    def put(self, request, pk):
        try:
            load = json.loads(json.dumps(request.data))
            user = ModelUser.objects.filter(id=pk)
            user.update(**load)
            check_update_user = ModelUser.objects.get(id=pk)
            serializer = UserSerializer(check_update_user)
            return JsonResponse({"users": serializer.data}, safe=False, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"error": str(e)})

    @swagger_auto_schema(responses={200: ReadOnlyUserSerializer()})
    def patch(self, request, pk):
        try:
            load = json.loads(json.dumps(request.data))
            user = ModelUser.objects.filter(id=pk)
            user.update(**load)
            check_update_user = ModelUser.objects.get(id=pk)
            serializer = UserSerializer(check_update_user)
            return JsonResponse({"users": serializer.data}, safe=False, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"error": str(e)})
