from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (CommentViewSet, FollowListCreate, GroupListCreate,
                    PostViewSet)

v1_router = DefaultRouter()
v1_router.register(r'posts', PostViewSet)
v1_router.register(r'posts/(?P<post_id>[0-9]+)/comments', CommentViewSet, basename='comments')





urlpatterns = [
    path('follow/', FollowListCreate.as_view()),
    path('group/', GroupListCreate.as_view()),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(v1_router.urls)),

]