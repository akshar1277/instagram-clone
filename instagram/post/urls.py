from post.views import index
from . import views
from django.urls import path


urlpatterns = [
    path('',index,name='index'),
    path('newpost/',views.NewPost,name='newpost'),
    path('<uuid:post_id>',views.PostDetails,name='postdetails'),
    path('tag/<slug:tag_slug>',views.tags,name='tags'),
    path('<uuid:post_id>/like',views.like,name='postlike')
]