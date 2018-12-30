from rest_framework.response import Response
from rest_framework.views import APIView

from photos.models import Photo
from photos.serializers import PhotoSerializer


class PhotoListAPI(APIView):

    def get(self, request):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)
