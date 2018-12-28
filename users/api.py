from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from users.serializers import UserSerializer


class UserListAPI(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        #serialized_users = serializer.data #lista de diccionarios
        #renderer = JSONRenderer()
        #json_users = renderer.render(serialized_users) #lista de diccionarios -> JSON
        #return HttpResponse(json_users)
        return Response(serializer.data)


class UserDetailAPI(APIView):

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk) #si el usuario existe me lo devuelve y sino me devuelve un 404
        serializer = UserSerializer(user)
        return Response(serializer.data)
