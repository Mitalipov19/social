from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import *

router=routers.DefaultRouter()

router.register(r'users',UserProfileViewSet,basename='user_list'),
router.register(r'post',PostViewSet,basename='post_list'),
router.register(r'follow',FollowViewSet,basename='follow_list'),
router.register(r'comment',CommentViewSet,basename='comment_list'),
router.register(r'comment-like',CommentLikeViewSet,basename='comment_like_list'),
router.register(r'story',StoryViewSet,basename='story_list'),
router.register(r'save',SaveViewSet,basename='save_list'),
router.register(r'save-item',SaveItemViewSet,basename='save_item_list'),

urlpatterns=[
    path('',include(router.urls)),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]

