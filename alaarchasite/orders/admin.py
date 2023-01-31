from django.contrib import admin
from orders.models import *

admin.site.register(YurtType)
admin.site.register(Yurt)
admin.site.register(YurtServices)
admin.site.register(OrderYurts)
admin.site.register(Hotel)
admin.site.register(HotelRoomType)
admin.site.register(HotelRoom)
admin.site.register(HotelServices)
admin.site.register(OrderHotelRooms)
admin.site.register(Zone)
admin.site.register(DependenceOfYurtServicesOnZones)
admin.site.register(DependenceOfHotelServicesOnHotels)
admin.site.register(Album)
admin.site.register(Images)
admin.site.register(News)
