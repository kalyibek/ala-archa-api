from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from orders.views import (
    YurtTypeAPIList,
    HotelsListAPI,
    HotelsAPIRetrieve,
    GeneralOrderYurtsAPIView,
    YurtOrderAPICreate,
    YurtOrderAPIRetrieve,
    YurtOrderAPIUpdate,
    YurtOrderAPIDelete,
    GeneralHotelRoomOrderAPIView,
    HotelRoomOrderAPICreate,
    HotelRoomOrderAPIRetrieve,
    HotelRoomOrderAPIUpdate,
    HotelRoomOrderAPIDelete,

    YurtTypeView,
    YurtView,
    YurtServiceView,
    HotelView,
    HotelRoomTypeView,
    HotelRoomView,
    HotelServiceView,
    ZoneCreateAPI,
    NewsAPICreate,
    NewsListAPIView,
    NewsAPIView,
    NewsAPIDelete,
    NewsAPIUpdate,
    ZoneCreateAPI,
    HotelServiceView
)

admin_patterns = [
    path('zone_create/', ZoneCreateAPI.as_view()),


    path('yurt_type/', YurtTypeView.as_view({'get': 'list'})),
    path('yurt_type/create/', YurtTypeView.as_view({'post': 'create'})),
    path('yurt_type/<int:pk>/', YurtTypeView.as_view({'get': 'retrieve'})),
    path('yurt_type/<int:pk>/update/', YurtTypeView.as_view({'put': 'update'})),
    path('yurt_type/<int:pk>/delete/', YurtTypeView.as_view({'delete': 'destroy'})),
    path('yurt/', YurtView.as_view({'get': 'list'})),
    path('yurt/create/', YurtView.as_view({'post': 'create'})),
    path('yurt/<int:pk>/', YurtView.as_view({'get': 'retrieve'})),
    path('yurt/<int:pk>/update/', YurtView.as_view({'put': 'update'})),
    path('yurt/<int:pk>/delete/', YurtView.as_view({'delete': 'destroy'})),
    path('yurt_service/', YurtServiceView.as_view({'get': 'list'})),
    path('yurt_service/create/', YurtServiceView.as_view({'post': 'create'})),
    path('yurt_service/<int:pk>/', YurtServiceView.as_view({'get': 'retrieve'})),
    path('yurt_service/<int:pk>/update/', YurtServiceView.as_view({'put': 'update'})),
    path('yurt_service/<int:pk>/delete/', YurtServiceView.as_view({'delete': 'destroy'})),
    path('hotels/', HotelView.as_view({'get': 'list'})),
    path('hotels/create/', HotelView.as_view({'post': 'create'})),
    path('hotels/<int:pk>/', HotelView.as_view({'get': 'retrieve'})),
    path('hotels/<int:pk>/update/', HotelView.as_view({'put': 'update'})),
    path('hotels/<int:pk>/delete/', HotelView.as_view({'delete': 'destroy'})),
    path('hotel_room_types/', HotelRoomTypeView.as_view({'get': 'list'})),
    path('hotel_room_types/create/', HotelRoomTypeView.as_view({'post': 'create'})),
    path('hotel_room_types/<int:pk>/', HotelRoomTypeView.as_view({'get': 'retrieve'})),
    path('hotel_room_types/<int:pk>/update/', HotelRoomTypeView.as_view({'put': 'update'})),
    path('hotel_room_types/<int:pk>/delete/', HotelRoomTypeView.as_view({'delete': 'destroy'})),
    path('hotel_rooms/', HotelRoomView.as_view({'get': 'list'})),
    path('hotel_rooms/create/', HotelRoomView.as_view({'post': 'create'})),
    path('hotel_rooms/<int:pk>/', HotelRoomView.as_view({'get': 'retrieve'})),
    path('hotel_rooms/<int:pk>/update/', HotelRoomView.as_view({'put': 'update'})),
    path('hotel_rooms/<int:pk>/delete/', HotelRoomView.as_view({'delete': 'destroy'})),
    path('hotel_services/', HotelServiceView.as_view({'get': 'list'})),
    path('hotel_services/create/', HotelServiceView.as_view({'post': 'create'})),
    path('hotel_services/<int:pk>/', HotelServiceView.as_view({'get': 'retrieve'})),
    path('hotel_services/<int:pk>/update/', HotelServiceView.as_view({'put': 'update'})),
    path('hotel_services/<int:pk>/delete/', HotelServiceView.as_view({'delete': 'destroy'})),
    path('yurts_orders/', GeneralOrderYurtsAPIView.as_view()),
    path('yurts_orders/<int:pk>/', YurtOrderAPIRetrieve.as_view()),
    path('yurts_orders/<int:pk>/update/', YurtOrderAPIUpdate.as_view()),
    path('yurts_orders/<int:pk>/delete/', YurtOrderAPIDelete.as_view()),
    path('rooms_orders/', GeneralHotelRoomOrderAPIView.as_view()),
    path('rooms_orders/<int:pk>/', HotelRoomOrderAPIRetrieve.as_view()),
    path('rooms_orders/<int:pk>/update/', HotelRoomOrderAPIUpdate.as_view()),
    path('rooms_orders/<int:pk>/delete/', HotelRoomOrderAPIDelete.as_view()),
    path('zone_create/', ZoneCreateAPI.as_view()),
]

urlpatterns = (
    [
        path('admin/', include(admin_patterns)),

        path('news/', include([
                path('', NewsListAPIView.as_view()),
                path('<int:pk>', include([
                    path('', NewsAPIView.as_view()),
                    path('update/', NewsAPIUpdate.as_view()),
                    path('delete/', NewsAPIDelete.as_view()),
                ])),
                path('create/', NewsAPICreate.as_view())
            ])),


        path('hotels_rooms/', HotelsListAPI.as_view()),
        path('hotels_rooms/<int:pk>/', HotelsAPIRetrieve.as_view()),

        path('order/yurt/create/', YurtOrderAPICreate.as_view()),
        path('order/yurt/<int:pk>/', YurtOrderAPIRetrieve.as_view()),
        path('order/hotel_room/create/', HotelRoomOrderAPICreate.as_view()),
        path('order/hotel_room/<int:pk>/', HotelRoomOrderAPIRetrieve.as_view()),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
