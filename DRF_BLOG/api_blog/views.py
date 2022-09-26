from rest_framework import generics
from blog.models import Post, Category
from .serializers import PostSerializer
from rest_framework import permissions #DjangoModelPermissionsOrAnonReadOnly #DjangoModelPermissions

# Create your views here.
class AuthorOrReadOnly(permissions.BasePermission):
    message = 'Editing and Deleting posts is restricted to the author only!'

    # def has_permission(self, request, view):
    #     if request.user.is_authenticated:
    #         return True
    #     return False

    # def has_object_permission(self, request, view, obj):
    #     if request.method in SAFE_METHODS:
    #         return True
    #     return obj.author == request.user

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


class PostDelete(generics.DestroyAPIView, AuthorOrReadOnly):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AuthorOrReadOnly]

class PostUpdate(generics.UpdateAPIView, AuthorOrReadOnly):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AuthorOrReadOnly]
