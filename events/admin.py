from django.contrib import admin
from events.models import Event


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = (
        'name',
        'date',
    )


admin.site.register(Event, EventAdmin)
