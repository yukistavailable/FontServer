from rest_framework import serializers
from ..models import BitMap


class CreateRetrieveBitMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitMap
        fields = [
            'value',
            'kanji',
            'memo',
        ]
