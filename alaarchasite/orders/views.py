from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import viewsets, generics, serializers, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import CustomUser
from .permissions import (
    IsAdminOrReadOnly,
    IsOwnerOrAdmin,
    IsOwnerOrReadOnly,
    IsOwner
)

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
    News,
)
from .serializers import (
    YurtTypeSerializer,
    YurtSerializer,
    OrderYurtsSerializer,
    YurtServiceSerializer,
    HotelSerializer,
    HotelRoomTypeSerializer,
    HotelRoomSerializer,
    HotelServiceSerializer,
    OrderHotelRoomSerializer,
    GeneralHotelSerializer,
    HotelRoomAdminSerializer,
    ZoneSerializer,
    ImgSerializer,
    NewsSerializer,
)
from users.serializers import CustomUserSerializer


class ImgAPICreate(generics.CreateAPIView):
    serializers = ImgSerializer


""" -------------/ Zones Views / ------------- """


class ZoneCreateAPI(APIView):

    def get(self, request, format=None):
        operators = CustomUser.objects.filter(is_staff=True)
        serializer = CustomUserSerializer(operators, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ZoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HotelsListAPI(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = GeneralHotelSerializer


class HotelsAPIRetrieve(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = GeneralHotelSerializer


""" -------------/ Yurts Order Views / ------------- """


class GeneralOrderYurtsAPIView(generics.ListAPIView):
    queryset = OrderYurts.objects.all()
    serializer_class = OrderYurtsSerializer
    permission_classes = [IsAdminUser]


class YurtOrderAPICreate(generics.CreateAPIView):
    queryset = OrderYurts.objects.all()
    serializer_class = OrderYurtsSerializer
    permission_classes = [IsAuthenticated]


class YurtOrderAPIRetrieve(generics.RetrieveAPIView):
    queryset = OrderYurts.objects.all()
    serializer_class = OrderYurtsSerializer
    permission_classes = [IsOwnerOrAdmin]


class YurtOrderAPIUpdate(generics.UpdateAPIView):
    queryset = OrderYurts.objects.all()
    serializer_class = OrderYurtsSerializer
    permission_classes = [IsAdminUser]


class YurtOrderAPIDelete(generics.DestroyAPIView):
    queryset = OrderYurts.objects.all()
    serializer_class = OrderYurtsSerializer
    permission_classes = [IsAdminUser]


""" -------------/ Order Hotel Rooms Views / ------------- """


class GeneralHotelRoomOrderAPIView(generics.ListAPIView):
    queryset = OrderHotelRooms.objects.all()
    serializer_class = OrderHotelRoomSerializer
    permission_classes = [IsAdminUser]


class HotelRoomOrderAPICreate(generics.CreateAPIView):
    queryset = OrderHotelRooms.objects.all()
    serializer_class = OrderHotelRoomSerializer
    permission_classes = [IsAuthenticated]


class HotelRoomOrderAPIRetrieve(generics.RetrieveAPIView):
    queryset = OrderHotelRooms.objects.all()
    serializer_class = OrderHotelRoomSerializer
    permission_classes = [IsOwnerOrAdmin]


class HotelRoomOrderAPIUpdate(generics.UpdateAPIView):
    queryset = OrderHotelRooms.objects.all()
    serializer_class = OrderYurtsSerializer
    permission_classes = [IsAdminUser]


class HotelRoomOrderAPIDelete(generics.DestroyAPIView):
    queryset = OrderHotelRooms.objects.all()
    serializer_class = OrderYurtsSerializer
    permission_classes = [IsAdminUser]


""" -------------/ Yurt Type Views / ------------- """


class YurtTypeAPIList(generics.ListCreateAPIView):
    queryset = YurtType.objects.all()
    serializer_class = YurtTypeSerializer
    permission_classes = [IsAdminOrReadOnly]


class YurtTypeAPIUpdate(generics.UpdateAPIView):
    queryset = YurtType.objects.all()
    serializer_class = YurtTypeSerializer
    permission_classes = [IsAdminOrReadOnly]


class YurtTypeAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = YurtType.objects.all()
    serializer_class = YurtTypeSerializer
    permission_classes = [IsAdminOrReadOnly]


# ----------------------------------------------------#

class YurtTypeView(viewsets.ModelViewSet):
    queryset = YurtType.objects.all()
    serializer_class = YurtTypeSerializer
    permission_classes = [IsAdminUser]


class YurtView(viewsets.ModelViewSet):
    queryset = Yurt.objects.all()
    serializer_class = YurtSerializer
    # permission_classes = [IsAdminUser]


class YurtServiceView(viewsets.ModelViewSet):
    queryset = YurtServices.objects.all()
    serializer_class = YurtServiceSerializer
    permission_classes = [IsAdminUser]


class HotelView(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAdminUser]


class HotelRoomTypeView(viewsets.ModelViewSet):
    queryset = HotelRoomType.objects.all()
    serializer_class = HotelRoomTypeSerializer
    permission_classes = [IsAdminUser]


class HotelRoomView(viewsets.ModelViewSet):
    queryset = HotelRoom.objects.all()
    serializer_class = HotelRoomAdminSerializer
    permission_classes = [IsAdminUser]


class HotelServiceView(viewsets.ModelViewSet):
    queryset = HotelServices.objects.all()
    serializer_class = HotelServiceSerializer
    permission_classes = [IsAdminUser]


""" -------------/ News Views / ------------- """


class NewsListAPIView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsAPIView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsAPICreate(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUser]


class NewsAPIUpdate(generics.UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUser]


class NewsAPIDelete(generics.DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUser]
