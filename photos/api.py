# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from photos.models import Photo
from photos.serializers import PhotoSerializer, PhotoListSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from photos.views import PhotosQueryset


class PhotoListAPI(PhotosQueryset, ListCreateAPIView):
    """
    Lista y crea las fotos (get y post)
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        return PhotoSerializer if self.request.method == "POST" else PhotoListSerializer

    def get_queryset(self):
        return self.get_photos_queryset(self.request)

    def perform_create(self, serializer):
        """
        Esta función es llamada antes de la llamada al serializer.save().
        Cada vez que guarda el objeto le asignará el propietario autenticado
        :param serializer:
        :return:
        """
        serializer.save(owner=self.request.user)

class PhotoDetailAPI(PhotosQueryset, RetrieveUpdateDestroyAPIView):
    """
    Detalle, actualización y borrado de fotos (get, put y delete)
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.get_photos_queryset(self.request)
