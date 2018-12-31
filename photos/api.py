# -*- coding: utf-8 -*-
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from photos.models import Photo
from photos.serializers import PhotoSerializer, PhotoListSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from photos.views import PhotosQueryset

class PhotoViewSet(PhotosQueryset, ModelViewSet):
    """
    Este Viewset hace los mismo que las clases PhotoListAPI y PhotoDetailAPI pero en una sola clase
    """
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'description', 'owner__first_name')
    ordering_fields = ('name', 'owner')

    def get_queryset(self):
        return self.get_photos_queryset(self.request)

    def get_serializer_class(self):
        if self.action == 'list':
            return PhotoListSerializer
        else:
            return PhotoSerializer

    def perform_create(self, serializer):
        """
        Asigna automáticamente la autoría de la nueva foto al usuario autenticado
        """
        serializer.save(owner=self.request.user)
