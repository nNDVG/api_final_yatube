from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import CommentViewSet, FollowListCreate, GroupListCreate, PostViewSet

v1_router = DefaultRouter()
v1_router.register(r'v1/posts', PostViewSet)
v1_router.register(r'v1/posts/(?P<post_id>[\d]+)/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/follow/', FollowListCreate.as_view()),
    path('v1/group/', GroupListCreate.as_view()),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(v1_router.urls)),

]
