from django.utils.html import format_html
from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "date", "location", "price", "preview_image")
    list_filter = ("category", "date")
    search_fields = ("title", "description")

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image.url)
        return "-"
    preview_image.short_description = "Image"
