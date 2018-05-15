# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'profiles', views.ProfileViewSet)
router.register(r'order', views.OrderViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
