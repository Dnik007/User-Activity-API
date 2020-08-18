from user_activity.models import User, UserActivity
from rest_framework.response import  Response
from rest_framework import viewsets
from rest_framework import permissions
from user_activity.serializers import UserSerializer, UserActivitySerializer


class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
