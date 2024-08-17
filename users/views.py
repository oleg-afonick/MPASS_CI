from .serializers import *
from rest_framework import viewsets


class PassUserViewSet(viewsets.ModelViewSet):
    queryset = PassUser.objects.all()
    serializer_class = PassUserSerializer
