from django.urls import path
from rest_framework.routers import DefaultRouter

from api_blog.views import PostDelete, PostDetail, PostList, PostUpdate

app_name = 'api_blog'

urlpatterns = [
    path('<slug:slug>/', PostDetail.as_view(), name='detailcreate'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='deletepost'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='updatepost'),
    path('', PostList.as_view(), name='listcreate'),
]

# router = DefaultRouter()
# router.register('',PostList, basename="user")
# urlpatterns = router.urls
