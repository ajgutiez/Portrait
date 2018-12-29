from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField() # solo lectura
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        """
        Crea una instancia de user a partir de una instance de validated_data que contiene valores deserializados
        :param validated_data: Diccionario con datos de usuario
        :return: objeto user
        """
        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        """
        Actualiza una instancia de user a partir de los datos del diccionario validated_data que contiene
        valores deserializados
        :param instance: objeto user a actualizar
        :param validated_data: diccionario con los nuevos valores para el user
        :return: objeto user actualizado
        """

        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()  # guardar en bd
        return instance

    def validate_username(selfself,data):
        """
        Valida si existe un usuario con ese username
        :param data:
        :return:
        """
        users = User.objects.filter(username=data)
        if len(users) != 0:
            raise serializers.ValidationError("Ya existe un usuario con ese username")
        else:
            return data