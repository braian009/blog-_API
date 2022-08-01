from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model

from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer
from .models import Post


# Create your views here.

class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(ModelViewSet):
    permission_classes = [IsAdminUser,]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
