import base64
import os
from PIL import Image
from django.utils.html import format_html
from django.contrib import admin

from .models import BitMap
from config.settings import BASE_DIR

BITMAP_DIR = os.getenv('BITMAP_DIR', 'main/bitmaps')
BITMAP_PATH = os.path.join(BASE_DIR, BITMAP_DIR)


class BitMapAdmin(admin.ModelAdmin):
    list_display = ('id', 'kanji', 'created_at', 'format_thumbnail',)
    list_display_links = ('id',)
    search_fields = ('kanji',)
    list_filter = ('kanji',)
    fields = ('id', 'kanji', 'value', 'created_at', 'format_image',)
    readonly_fields = ('id', 'created_at', 'format_image', 'format_thumbnail',)

    def format_image(self, obj):
        img_path = os.path.join(BITMAP_PATH, str(obj.id) + '.png')
        # img to base64
        if not os.path.exists(img_path):
            return None

        with open(img_path, 'rb') as f:
            img = f.read()
        img_base64 = base64.b64encode(img).decode('utf-8')
        return format_html(
            f'<img width=800 height=800 src="data:image/png;base64,{img_base64}" />')

    def format_thumbnail(self, obj):
        img_path = os.path.join(BITMAP_PATH, str(obj.id) + '.png')
        # img to base64
        if not os.path.exists(img_path):
            return None

        with open(img_path, 'rb') as f:
            img = f.read()
        img_base64 = base64.b64encode(img).decode('utf-8')
        return format_html(
            f'<img width=80 height=80 src="data:image/png;base64,{img_base64}" />')


admin.site.register(BitMap, BitMapAdmin)
