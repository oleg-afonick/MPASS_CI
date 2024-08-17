from rest_framework import serializers
from .models import *


class PassUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassUser
        fields = ('email', 'firstname', 'lastname', 'surname', 'phone',)

    def create(self, validated_data):
        self.is_valid()
        pass_user = PassUser.objects.filter(email=self.validated_data.get('email'))
        if pass_user.exists():
            return pass_user.first()
        else:
            return PassUser.objects.create(
                email=self.validated_data.get('email'),
                firstname=self.validated_data.get('firstname'),
                lastname=self.validated_data.get('lastname'),
                surname=self.validated_data.get('surname'),
                phone=self.validated_data.get('phone'),
            )
