from django.db import models
from django.contrib.auth.models import Group
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from djmoney.models.fields import MoneyField


def car_picture_upload_to(car: "Car", filename: str) -> str:
    return f"{car.group.pk}/cars/{filename}"


class Car(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
    )
    make = models.CharField(
        _("Make"),
        max_length=100,
    )
    model = models.CharField(
        _("Model"),
        max_length=100,
    )
    year = models.PositiveSmallIntegerField(
        _("Year"),
    )
    vin = models.CharField(
        _("VIN"),
        max_length=100,
    )
    license = models.CharField(
        _("License plate"),
        max_length=32,
    )
    description = models.TextField(
        _("Description"),
        blank=True,
    )
    picture = models.FileField(
        _("Photo"),
        upload_to=car_picture_upload_to,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.year} {self.make} {self.model} ({self.license})"


class Record(models.Model):
    # Record Types
    NOTE = 0
    OWNERSHIP = 1
    GAS = 2
    MAINTENANCE = 3

    TYPE_CHOICES = (
        (NOTE, _("Note")),
        (OWNERSHIP, _("Ownership change")),
        (GAS, _("Gasoline")),
        (MAINTENANCE, _("Maintenance")),
    )

    car = models.ForeignKey(
        Car,
        related_name="records",
        on_delete=models.CASCADE,
    )
    type = models.SmallIntegerField(
        _("Record Type"),
        choices=TYPE_CHOICES,
    )
    timestamp = models.DateTimeField(
        _("Timestamp"),
        default=timezone.now,
    )
    odometer = models.PositiveIntegerField(
        _("Odometer reading"),
    )
    cost = MoneyField(
        _("Cost"),
        decimal_places=2,
        max_digits=10,
        default_currency="USD",
        null=True,
    )
    description = models.CharField(
        _("Description"),
        max_length=255,
    )
    notes = models.TextField(
        _("Notes"),
        blank=True,
    )

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self) -> str:
        timestamp = timezone.localtime(self.timestamp)
        return (
            f"{self.car} - {self.get_type_display()}: {self.description} ({timestamp})"
        )


def record_file_upload_to(file: "RecordFile", filename: str) -> str:
    return f"{file.record.car.group.pk}/records/{file.record.pk}/{filename}"


class RecordFile(models.Model):
    record = models.ForeignKey(
        Record,
        on_delete=models.CASCADE,
        related_name="files",
    )
    file = models.FileField(
        _("File"),
        upload_to=record_file_upload_to,
    )
    description = models.CharField(
        _("Description"),
        max_length=255,
        blank=True,
    )
