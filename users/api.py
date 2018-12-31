from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from users.serializers import UserSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


class UserListAPI(APIView):

    def get(self, request):
        """
        Obtiene el listado de usuarios
        :param request:
        :return:
        """
        #instancia del paginador
        paginator = PageNumberPagination()
        users = User.objects.get_queryset().order_by('id')
        #paginar el queryset
        paginator.paginate_queryset(users, request)
        serializer = UserSerializer(users, many=True)
        #devolver respuesta paginada
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        """
        Crea un nuevo usuario
        :param request:
        :return:
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPI(APIView):

    def get(self, request, pk):
        """
        Devuelve el usuario dado su id
        :param request:
        :param pk:
        :return:
        """
        user = get_object_or_404(User, pk=pk) #si el usuario existe me lo devuelve y sino me devuelve un 404
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Actualiza usuario con los datos
        :param request:
        :param pk:
        :return:
        """
        user = get_object_or_404(User, pk=pk)  # si el usuario existe me lo devuelve y sino me devuelve un 404
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Borra un usuario de la bd
        :param request:
        :param pk:
        :return:
        """
        user = get_object_or_404(User, pk=pk)  # si el usuario existe me lo devuelve y sino me devuelve un 404
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)