from rest_framework import generics
from .models import User
from .serializers import UserSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('legacy_id')
    serializer_class = UserSerializer
