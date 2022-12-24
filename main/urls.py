from django.urls import path
from .views.bitmap_views import PostGetBitMapView

urlpatterns = [
    path('bitmap', PostGetBitMapView.as_view()),
    path('bitmap/<pk>', PostGetBitMapView.as_view()),
]
