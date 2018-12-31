
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from photos.api import PhotoViewSet


#APIRouter
router = DefaultRouter()
router.register(r'photos', PhotoViewSet)

urlpatterns = [
    #API Urls
    url(r'1.0/', include(router.urls)),  #incluyo las URLS de API
]