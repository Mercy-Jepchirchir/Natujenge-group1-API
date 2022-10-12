from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BillModelViewSet

router = DefaultRouter()
router.register("", BillModelViewSet, basename="bills")

urlpatterns = [
    path("", include(router.urls)),
]