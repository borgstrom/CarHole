from django.contrib import admin

from cars.models import Car, Record, RecordFile


class RecordFileInline(admin.StackedInline):
    model = RecordFile
    extra = 1


class RecordAdmin(admin.ModelAdmin):
    date_hierarchy = "timestamp"
    list_display = [
        "type",
        "car",
        "timestamp",
        "odometer",
        "cost",
        "description",
    ]
    list_filter = [
        "car",
        "type",
    ]
    search_fields = [
        "description",
        "notes",
    ]
    inlines = [
        RecordFileInline,
    ]


admin.site.register(Car)
admin.site.register(Record, RecordAdmin)
