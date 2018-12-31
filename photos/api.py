from rest_framework.generics import ListCreateAPIView
from photos.models import Photo
from photos.serializers import PhotoSerializer


class PhotoListAPI(ListCreateAPIView):
    """
    Lista y crea las fotos (get y post)
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
