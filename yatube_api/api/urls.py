from rest_framework import routers

from django.urls import path, include

from api.views import PostViewSet, GroupViewSet, CommentViewSet
from api.views import FollowViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('api/v1/', include('djoser.urls.jwt')),
]
