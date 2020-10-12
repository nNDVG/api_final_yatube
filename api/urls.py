from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (CommentViewSet, FollowListCreate, GroupListCreate,
                    PostViewSet)

v1_router = DefaultRouter()
v1_router.register(r'posts', PostViewSet)
v1_router.register(r'posts/(?P<post_id>[\d]+)/comments', CommentViewSet, basename='comments')

paths = ([
    path('follow/', FollowListCreate.as_view()),
    path('group/', GroupListCreate.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
])

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include(paths)),

]
