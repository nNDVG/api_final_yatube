from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions
from rest_framework.viewsets import ModelViewSet

from api.serializers import (CommentSerializer, FollowSerializer,
                             GroupSerializer, PostSerializer)

from .models import Follow, Group, Post
from .permissions import IsOwnerOrReadOnly


class PostViewSet(ModelViewSet):
    """
    ViewSet for operations with posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    """
    ViewSet for operations with comments.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return post.comments.all()

    def perform_create(self, serializer):
        get_object_or_404(Post, id=self.kwargs['post_id'])
        serializer.save(author=self.request.user)


class GroupListCreate(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FollowListCreate(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__username', '=following__username']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)










