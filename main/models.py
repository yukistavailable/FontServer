from django.db import models

# Create your models here.


class BitMap(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    value = models.CharField(null=False, blank=False, max_length=50000)
    kanji = models.CharField(null=False, max_length=1, default='魚')
    memo = models.TextField(null=True, blank=True, max_length=1000)
