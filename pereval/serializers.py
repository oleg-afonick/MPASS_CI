from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from users.serializers import PassUserSerializer
from .models import *


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height',)


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('winter', 'summer', 'autumn', 'spring',)


class ImagesSerializer(serializers.ModelSerializer):
    data = serializers.URLField()

    class Meta:
        model = Images
        fields = ('data', 'title',)


class PerevalSerializer(WritableNestedModelSerializer):
    user = PassUserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImagesSerializer(many=True)

    class Meta:
        model = Pereval
        depth = 1
        fields = (
            'id', 'user', 'beauty_title', 'title', 'other_titles', 'connect', 'coords', 'level', 'images', 'status')

    def create(self, validated_data, **kwargs):
        user = validated_data.pop('user')
        print(user)
        coords = validated_data.pop('coords')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        pass_user = PassUser.objects.filter(email=user['email'])
        if pass_user.exists():
            user_serializer = PassUserSerializer(data=user)
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()

        else:
            user = PassUser.objects.create(**user)
        coords = Coords.objects.create(**coords)
        level = Level.objects.create(**level)
        pereval = Pereval.objects.create(**validated_data, user=user, coords=coords, level=level, status='new')

        for image in images:
            data = image.pop('data')
            title = image.pop('title')
            Images.objects.create(data=data, pereval=pereval, title=title)

        return pereval

    def validate(self, data):
        if self.instance is not None:
            instance_user = self.instance.user
            data_user = data.get('user')
            validating_user_fields = [
                instance_user.lastname != data_user['lastname'],
                instance_user.firstname != data_user['firstname'],
                instance_user.surname != data_user['surname'],
                instance_user.phone != data_user['phone'],
                instance_user.email != data_user['email'],
            ]
            if data_user is not None and any(validating_user_fields):
                raise serializers.ValidationError({'Отклонено': 'Нельзя изменять данные пользователя'})
        return data
