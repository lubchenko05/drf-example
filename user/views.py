from rest_framework.generics import CreateAPIView, UpdateAPIView

from user.models import CustomUser
from user.serializers import UserSerializer


class CreateUser(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UpdateUser(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
