"""m_pass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pereval.views import *
from users.views import *
from rest_framework import routers
from pereval.views import PerevalViewSet
from .yasg import urlpatterns as doc_urls

router = routers.SimpleRouter()
router.register(r'user', PassUserViewSet, basename='user')
router.register(r'coords', CoordsViewSet, basename='coords')
router.register(r'level', LevelViewSet, basename='level')
router.register(r'images', ImagesViewSet, basename='images')
router.register(r'pereval', PerevalViewSet, basename='pereval')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

urlpatterns += doc_urls

