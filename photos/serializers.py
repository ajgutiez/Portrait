from rest_framework import serializers
from models import Photo

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = '__all__'
        #read_only_field = ('owner',)


class PhotoListSerializer(PhotoSerializer):
    class Meta(PhotoSerializer.Meta):
        fields = ('id', 'name', 'url')