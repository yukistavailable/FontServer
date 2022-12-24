import os
import json

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, views

# from ..models import BitMap
from ..models import BitMap
from ..serializers.bitmap_serializers import CreateRetrieveBitMapSerializer
from config.settings import BASE_DIR

BITMAP_DIR = os.getenv('BITMAP_DIR', 'main/bitmaps')
BITMAP_PATH = os.path.join(BASE_DIR, BITMAP_DIR)

if not os.path.exists(BITMAP_PATH):
    os.makedirs(BITMAP_PATH)


def save_bitmap_to_json(id, value, kanji):
    gray_scale_values = value.split(',')
    gray_scale_values = [int(v) for v in gray_scale_values]
    bitmap = {
        'kanji': kanji,
        'value': gray_scale_values,
    }
    bitmap_path = os.path.join(BITMAP_PATH, str(id) + '.json')
    with open(bitmap_path, 'w') as f:
        json.dump(bitmap, f)


class PostGetBitMapView(views.APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def get(self, request, pk, *args, **kwargs):
        try:
            bit_map = BitMap.objects.get(id=pk)
        except BaseException:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CreateRetrieveBitMapSerializer(instance=bit_map)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        print('post--------------------------------------')
        try:
            serializer = CreateRetrieveBitMapSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                created_bit_map = serializer.save()
                save_bitmap_to_json(
                    created_bit_map.id,
                    created_bit_map.value,
                    created_bit_map.kanji)
                return Response(
                    created_bit_map.id,
                    status=status.HTTP_201_CREATED)
        except BaseException as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
