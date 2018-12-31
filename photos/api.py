# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from photos.models import Photo
from photos.serializers import PhotoSerializer


class PhotoListAPI(ListCreateAPIView):
    """
    Lista y crea las fotos (get y post)
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Detalle, actualización y borrado de fotos (get, put y delete)
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
