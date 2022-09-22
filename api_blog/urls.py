from django.urls import path

from api_blog.views import PostDelete, PostDetail, PostList, PostUpdate

app_name = 'api_blog'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='deletepost'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='updatepost'),
    path('', PostList.as_view(), name='listcreate'),
]