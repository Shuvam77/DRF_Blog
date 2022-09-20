from rest_framework import generics
from blog.models import Post, Category
from .serializers import PostSerializer
from rest_framework import permissions

# Create your views here.
class AuthorOrReadOnly(permissions.BasePermission):

    # def has_permission(self, request, view):
    #     if request.user.is_authenticated:
    #         return True
    #     return False

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False

class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

    

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDelete(generics.DestroyAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    permission_classes = [AuthorOrReadOnly]
