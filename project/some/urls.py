from django.contrib import admin
from django.urls import path, include
from .views import (
    Posts, Post, PostCreate, PostUpdate, post_comment, MyCommets, MyCommentsDelete, MyCommentDetail
)

urlpatterns = [
    path('', Posts.as_view(), name='posts'),
    path('<int:pk>', Post.as_view(), name='post'),
    path('create/', PostCreate.as_view(), name='postcreate'),
    path('<int:pk>/update', PostUpdate.as_view(), name='postupdate'),
    path('<int:pk>/comment', post_comment, name='postcomment'),
    path('comments/', MyCommets.as_view(), name='comments'),
    path('comments/<int:pk>', MyCommentDetail.as_view(), name='comment'),
    path('comments/<int:pk>/delete', MyCommentsDelete.as_view(), name='commentdelete'),
]
