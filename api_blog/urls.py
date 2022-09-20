from django.urls import path

from api_blog.views import PostDelete, PostDetail, PostList

app_name = 'api_blog'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='deletepost'),
    path('', PostList.as_view(), name='listcreate'),
]