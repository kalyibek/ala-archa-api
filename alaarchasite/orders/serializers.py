from abc import ABC

from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from users.models import CustomUser
from users.serializers import CustomUserSerializer
from .models import (
    YurtType,
    Yurt,
    OrderYurts,
    YurtServices,
    Hotel,
    HotelRoomType,
    HotelRoom,
    HotelServices,
    OrderHotelRooms,
    Zone,
    DependenceOfYurtServicesOnZones,
    DependenceOfHotelServicesOnHotels,
    Album,
    Images,
    News,
)


class ImgSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Images.objects.create(**validated_data)

    class Meta:
        model = Images
        fields = "__all__"


class AlbSerializer(serializers.ModelSerializer):
    images = ImgSerializer(many=True)

    class Meta:
        model = Album
        fields = '__all__'

    def create(self, validated_data):
        return Album.objects.create(**validated_data)


class YurtTypeSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return YurtType.objects.create(**validated_data)

    class Meta:
        model = YurtType
        fields = '__all__'


class YurtSerializer(serializers.ModelSerializer):
    album = AlbSerializer(read_only=True)

    def create(self, validated_data):
        return Yurt.objects.create(**validated_data)

    class Meta:
        model = Yurt
        fields = '__all__'


class ZoneSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        new_zone = Zone.objects.create(
            designation=validated_data['designation'],
            description=validated_data['description'],
            quantity_of_yurts=validated_data['quantity_of_yurts'],
            operator=validated_data['operator']
        )
        return new_zone

    class Meta:
        model = Zone
        fields = '__all__'


class DependenceOfYurtServicesOnZonesSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return DependenceOfYurtServicesOnZones.objects.create(**validated_data)

    class Meta:
        model = DependenceOfYurtServicesOnZones
        fields = '__all__'


class OrderYurtsSerializer(serializers.ModelSerializer):
    clientId = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = OrderYurts
        fields = '__all__'
        read_only_fields = ['clientId']

    def create(self, validated_data):
        user = self.context['request'].user
        new_yurt_order = OrderYurts.objects.create(
            clientId=user,
            yurtId=validated_data['yurtId'],
            reservationStartDateTime=validated_data['reservationStartDateTime'],
            reservationEndDateTime=validated_data['reservationEndDateTime'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            status='booked'
        )

        return new_yurt_order


class YurtServiceSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return YurtServices.objects.create(**validated_data)

    class Meta:
        model = YurtServices
        fields = '__all__'


class HotelServiceSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return HotelServices.objects.create(**validated_data)

    class Meta:
        model = HotelServices
        fields = '__all__'


class DependenceOfHotelServicesOnHotelsSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return DependenceOfHotelServicesOnHotels.objects.create(**validated_data)

    class Meta:
        model = DependenceOfHotelServicesOnHotels
        fields = ['hotel_service', 'hotel', 'price']


class HotelSerializer(serializers.ModelSerializer):
    album = AlbSerializer(read_only=True)

    def create(self, validated_data):
        return Hotel.objects.create(**validated_data)

    class Meta:
        model = Hotel
        fields = "__all__"


class HotelRoomTypeSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return HotelRoomType.objects.create(**validated_data)

    class Meta:
        model = HotelRoomType
        fields = '__all__'


class HotelRoomSerializer(serializers.ModelSerializer):
    album = AlbSerializer(read_only=True)

    hotel_room_typeId = HotelRoomTypeSerializer()

    def create(self, validated_data):
        return HotelRoom.objects.create(**validated_data)

    class Meta:
        model = HotelRoom
        fields = '__all__'


class HotelRoomAdminSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return HotelRoom.objects.create(**validated_data)

    class Meta:
        model = HotelRoom
        fields = '__all__'


class OrderHotelRoomSerializer(serializers.ModelSerializer):
    clientId = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = OrderHotelRooms
        fields = '__all__'
        read_only_fields = ['clientId']

    def create(self, validated_data):
        user = self.context['request'].user
        new_room_order = OrderHotelRooms.objects.create(
            clientId=user,
            roomId=validated_data['roomId'],
            reservationStartDate=validated_data['reservationStartDate'],
            reservationEndDate=validated_data['reservationEndDate'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            status=validated_data['status']
        )

        return new_room_order


class GeneralHotelSerializer(serializers.ModelSerializer):
    rooms = HotelRoomSerializer(many=True)
    services = HotelServiceSerializer(many=True)

    class Meta:
        model = Hotel
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    album = AlbSerializer(read_only=True)

    class Meta:
        model = News
        fields = ['name', 'title', 'text', 'album', 'status']
