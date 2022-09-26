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

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

    # def has_object_permission(self, request, view, obj):
    #     if obj.author == request.user:
    #         return True
    #     return False

class PostList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDelete(generics.DestroyAPIView, AuthorOrReadOnly):
    permission_classes = [AuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostUpdate(generics.UpdateAPIView, AuthorOrReadOnly):
    permission_classes = [AuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


""" Concrete View Classes
# CreateAPIView
Used for create-only endpoints.
# ListAPIView
Used for read-only endpoints to represent a collection of model instances.
# RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
# DestroyAPIView
Used for delete-only endpoints for a single model instance.
# UpdateAPIView
Used for update-only endpoints for a single model instance.
# ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
# RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
# RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""