from django.db import models
from users.models import CustomUser
from django.utils import timezone

STATUS_CHOICES_PAID = 'paid'
STATUS_CHOICES_BOOKED = 'booked'
STATUS_CHOICES_CANCELED = 'canceled'


# -------------/ Album Models / ------------- #

def get_upload_path(instance, filename):
    model = Album
    name = model.verbose_name_plural.replace(' ', '_')
    return f'{name}/images/{filename}'


class Album(models.Model):
    verbose_name_plural = "Albums"
    name = models.CharField(max_length=2000, verbose_name='Название')

    def __str__(self):
        return self.name

    def default(self):
        return self.images.filter(default=True).first()

    def thumbnails(self):
        return self.images.filter(width__lt=100, lenght_lt=100)


class Images(models.Model):
    album = models.ForeignKey(Album, related_name='images', on_delete=models.CASCADE, default="Gleb")
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_upload_path)
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)


# -------------/ Yurt Models / ------------- #


class YurtType(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class YurtServices(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=250)

    def __str__(self):
        return (
            f'service: {self.name}'
        ).format()


class Zone(models.Model):
    designation = models.CharField(max_length=25, unique=True, verbose_name="название зоны")
    description = models.TextField(verbose_name="описание зоны")
    quantity_of_yurts = models.PositiveSmallIntegerField(verbose_name="количество тапчанов в зоне")
    operator = models.OneToOneField(CustomUser, null=True, on_delete=models.SET_NULL,
                                    related_name="zone", verbose_name="оператор ответственный за зону")
    yurts_services = models.ManyToManyField(YurtServices, through="DependenceOfYurtServicesOnZones")

    def __str__(self):
        return self.designation


class Yurt(models.Model):
    type = models.ForeignKey(YurtType, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    album = models.ForeignKey(Album, related_name='yurt', on_delete=models.CASCADE, blank=True, null=True)
    zone = models.ForeignKey(Zone, null=True, on_delete=models.SET_NULL, related_name="yurt_zone"
                             , verbose_name="зона в которой находится")


class OrderYurts(models.Model):
    STATUS_CHOICES = [
        (STATUS_CHOICES_PAID, 'Заказ оплачен'),
        (STATUS_CHOICES_BOOKED, 'Забронировано'),
        (STATUS_CHOICES_CANCELED, 'Заказ отменен'),
    ]
    clientId = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    yurtId = models.ForeignKey(Yurt, on_delete=models.CASCADE)
    reservationStartDateTime = models.DateTimeField()
    reservationEndDateTime = models.DateTimeField()
    first_name = models.CharField(max_length=25, null=True)
    last_name = models.CharField(max_length=25, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_CHOICES_BOOKED, null=True)

    def __str__(self):
        return (
            f'customer: '
            f'{self.first_name}\n'
            f'{self.last_name}'
        ).format()


# -------------/ Hotel Models / ------------- #
class HotelRoomType(models.Model):
    name = models.CharField(max_length=25)
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return (
            f'{self.name}\n'
            f'{str(self.price_per_day)} som'
        ).format()


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    album = models.ForeignKey(Album, related_name='hotel', on_delete=models.CASCADE, blank=True, null=True)
    zone = models.ForeignKey(Zone, null=True, on_delete=models.SET_NULL, related_name="hotel_zone"
                             , verbose_name="зона в которой находится отель")

    def __str__(self):
        return self.name


class HotelRoom(models.Model):
    room_number = models.IntegerField()
    hotel_room_typeId = models.ForeignKey(HotelRoomType, on_delete=models.CASCADE)
    hotelId = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, related_name='rooms')
    description = models.TextField(max_length=250)
    album = models.ForeignKey(Album, related_name='hotel_room', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return (
            f'room {str(self.room_number)}'
        ).format()


class HotelServices(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=250)
    hotelId = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='services', null=True)

    def __str__(self):
        return (
            f'service: {self.name}'
        ).format()


class OrderHotelRooms(models.Model):
    STATUS_CHOICES = [
        (STATUS_CHOICES_PAID, 'Заказ оплачен'),
        (STATUS_CHOICES_BOOKED, 'Забронировано'),
        (STATUS_CHOICES_CANCELED, 'Заказ отменен'),
    ]
    clientId = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    roomId = models.ForeignKey(HotelRoom, on_delete=models.CASCADE)
    reservationStartDate = models.DateField()
    reservationEndDate = models.DateField()
    first_name = models.CharField(max_length=25, null=True)
    last_name = models.CharField(max_length=25, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_CHOICES_BOOKED, null=True)

    def __str__(self):
        return (
            f'customer: '
            f'{self.first_name}\n'
            f'{self.last_name}'
        ).format()


# -------------/ Zones / ------------- #


class DependenceOfYurtServicesOnZones(models.Model):
    yurt_service = models.ForeignKey(YurtServices, on_delete=models.CASCADE, verbose_name="услуга")
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, verbose_name="зона услуги")
    price = models.PositiveSmallIntegerField(verbose_name="цена за услугу в данной зоне")


class DependenceOfHotelServicesOnHotels(models.Model):
    hotel_service = models.ForeignKey(HotelServices, on_delete=models.CASCADE, verbose_name="услуга отеля")
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name="отель")
    price = models.PositiveSmallIntegerField(verbose_name="цена за услугу в данном отеле")


# -------------/ News Models / ------------- #

STATUS_CHOICES = [
    ('new', 'Новый'),
    ('moderated', 'Модерировано'),
    ('rejected', 'Отклонено')
]


class News(models.Model):
    name = models.CharField(max_length=2000, verbose_name='Название')
    title = models.CharField(max_length=2000, verbose_name='Описание')
    text = models.CharField(max_length=2000, verbose_name='Текст')
    album = models.ForeignKey(Album, related_name='news', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    publish_at = models.DateTimeField(verbose_name="Время публикации", blank=True, default=timezone.now)
    status = models.CharField(null=True, blank=True, max_length=15, choices=STATUS_CHOICES, default='new',
                              verbose_name='Статус')

    def save(self, **kwargs):
        if not self.publish_at:
            if not self.pk:
                self.publish_at = timezone.now()
            else:
                self.publish_at = News.objects.get(pk=self.pk).publish_at
        super().save(**kwargs)

    def __str__(self):
        return "{}. {}".format(self.pk, self.name)

    class Meta:
        # permissions = [('moderator', 'Модератор')]
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
