from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
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

# class PostList(viewsets.ModelViewSet):
#     serializer_class = PostSerializer
#     permission_classes = [AuthorOrReadOnly]

#     def get_object(self, query=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)

#     def get_queryset(self):
#         return Post.objects.all()
    

class PostList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class PostDelete(AuthorOrReadOnly, generics.DestroyAPIView):
    permission_classes = [AuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class PostUpdate(AuthorOrReadOnly, generics.UpdateAPIView):
    permission_classes = [AuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'



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


# class UserViewSet(viewsets.ViewSet):
#     """
#     Example empty viewset demonstrating the standard
#     actions that will be handled by a router class.

#     If you're using format suffixes, make sure to also include
#     the `format=None` keyword argument for each action.
#     """

#     def list(self, request):
#         pass

#     def create(self, request):
#         pass

#     def retrieve(self, request, pk=None):
#         pass

#     def update(self, request, pk=None):
#         pass

#     def partial_update(self, request, pk=None):
#         pass

#     def destroy(self, request, pk=None):
#         pass