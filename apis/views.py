from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import BillSerializer
from .models import Bill
# Create your views here.
class BillModelViewSet(ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
