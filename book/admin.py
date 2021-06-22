from django.contrib import admin

# Register your models here.


from .models import Flight


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    """
    Admin for IncidentType model
    """
    list_filter = ('start_date', 'return_date')
    list_display = ('id', 'beginning', 'destination', 'start_date', 'return_date', 'adult', 'children')
    ordering = ('-start_date',)
    search_fields = ('beginning', 'destination', 'start_date')