from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (CommentViewSet, FollowList, GroupList,
                    PostViewSet)

v1_router = DefaultRouter()
v1_router.register(r'posts', PostViewSet)
v1_router.register(r'posts/(?P<post_id>[\d]+)/comments', CommentViewSet, basename='comments')
v1_router.register(r'follow', FollowList)
v1_router.register(r'group', GroupList)

paths = ([
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
])

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include(paths)),

]
