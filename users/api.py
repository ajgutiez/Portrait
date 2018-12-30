from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from users.serializers import UserSerializer
from rest_framework import status


class UserListAPI(APIView):

    def get(self, request):
        """
        Obtiene el listado de usuarios
        :param request:
        :return:
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        #serialized_users = serializer.data #lista de diccionarios
        #renderer = JSONRenderer()
        #json_users = renderer.render(serialized_users) #lista de diccionarios -> JSON
        #return HttpResponse(json_users)
        return Response(serializer.data)

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