from django.contrib.auth.models import User
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from users.serializers import UserSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from users.permissions import UserPermission
from rest_framework.viewsets import ViewSet

class UserViewSet(ViewSet):


    permission_classes = (UserPermission,)

    def list(self, request):
        """
        Obtiene el listado de usuarios
        :param request:
        :return:
        """
        self.check_permissions(request)
        #instancia del paginador
        paginator = PageNumberPagination()
        users = User.objects.get_queryset().order_by('id')
        #paginar el queryset
        paginator.paginate_queryset(users, request)
        serializer = UserSerializer(users, many=True)
        #devolver respuesta paginada
        return paginator.get_paginated_response(serializer.data)

    def create(self, request):
        """
        Crea un nuevo usuario
        :param request:
        :return:
        """
        self.check_permissions(request)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        """
        Devuelve el usuario dado su id
        :param request:
        :param pk:
        :return:
        """
        self.check_permissions(request)
        user = get_object_or_404(User, pk=pk) #si el usuario existe me lo devuelve y sino me devuelve un 404
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk):
        """
        Actualiza usuario con los datos
        :param request:
        :param pk:
        :return:
        """
        self.check_permissions(request)
        user = get_object_or_404(User, pk=pk)  # si el usuario existe me lo devuelve y sino me devuelve un 404
        self.check_object_permissions(request, user)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        """
        Borra un usuario de la bd
        :param request:
        :param pk:
        :return:
        """
        self.check_permissions(request)
        user = get_object_or_404(User, pk=pk)  # si el usuario existe me lo devuelve y sino me devuelve un 404
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)