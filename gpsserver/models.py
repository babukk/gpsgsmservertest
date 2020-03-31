
from django.db import models
from django.contrib.gis.db import models as gis_models
from django.utils import timezone

from users.models import CustomUser

# модель 'Транспортное средство'
class Transport(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name="Пользователь")
    name = models.CharField(max_length=120, verbose_name="Наименование")

    class Meta:
        verbose_name_plural = "Транспортные средства"
        verbose_name = "Транспортное средство"

# модель 'Данные Транспортного средства'
class TransportData(models.Model):
    user = models.ForeignKey(Transport, on_delete=models.PROTECT, verbose_name="Транспортное средство")
    # lattitude = models.DecimalField(verbose_name="Широта", max_digits=24, decimal_places=7)
    # longitude = models.DecimalField(verbose_name="Долгота", max_digits=24, decimal_places=7)
    point = gis_models.GeometryField(geography=True, verbose_name="Точка на карте", blank=True, null=True, default=None)
    altitude = models.IntegerField(verbose_name="Высота над уровнем моря", blank=True, null=True, default=None)
    when_added = models.DateTimeField(default=timezone.now, verbose_name="Дата-время добавления записи")
    speed = models.DecimalField(verbose_name="Скорость", max_digits=7, decimal_places=2, blank=True, null=True, default=None)
    satellites = models.IntegerField(verbose_name="Спутники", blank=True, null=True, default=None)
    flags1 = models.IntegerField(verbose_name="Флаги 1", blank=True, null=True, default=None)
    flags2 = models.IntegerField(verbose_name="Флаги 2", blank=True, null=True, default=None)
    flags3 = models.IntegerField(verbose_name="Флаги 3", blank=True, null=True, default=None)

    class Meta:
        verbose_name_plural = "Данные транспортных средств"
        verbose_name = "Данные транспортного средства"
