from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all().order_by('legacy_id')
    serializer_class = OrderSerializer
