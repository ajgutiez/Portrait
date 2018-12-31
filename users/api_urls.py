# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from users.api import UserViewSet

#APIRouter
router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='user') #se le añade base_name porque no lleva queryset

urlpatterns = [
    #API Urls
    url(r'1.0/', include(router.urls)),  #incluyo las URLS de API
]