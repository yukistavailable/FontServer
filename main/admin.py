from django.contrib import admin
from .models import BitMap

# Register your models here.


class BitMapAdmin(admin.ModelAdmin):
    list_display = ('id', 'kanji', 'created_at')
    list_display_links = ('id',)
    search_fields = ('kanji',)
    list_filter = ('kanji',)


admin.site.register(BitMap, BitMapAdmin)
