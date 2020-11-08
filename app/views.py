from django.shortcuts import render
from app.models import Post, Category
from app.serializers import PostSerializer, PostSerializerWrite, \
        CategorySerializer, AuthorSerializer
from django.contrib.auth.models import User
from rest_framework import generics


# Create your views here.
class MethodSerializerView(object):
    '''
    Utility class for get different serializer class by method.
    For example:
    method_serializer_classes = {
        ('GET', ): MyModelListViewSerializer,
        ('PUT', 'PATCH'): MyModelCreateUpdateSerializer
    }
    '''
    method_serializer_classes = None

    def get_serializer_class(self):
        assert self.method_serializer_classes is not None, (
            'Expected view %s should contain method_serializer_classes '
            'to get right serializer class.' %
            (self.__class__.__name__, )
        )
        for methods, serializer_cls in self.method_serializer_classes.items():
            if self.request.method in methods:
                return serializer_cls

        raise exceptions.MethodNotAllowed(self.request.method)


class PostList(MethodSerializerView, generics.ListCreateAPIView):  
    """
    API: /
    Methods: GET/POST
    """
    queryset = Post.objects.all()
    method_serializer_classes = {
            ('GET', ): PostSerializer,
            ('POST'): PostSerializerWrite,
    }
    #serializer_class = PostSerializer


class PostDetail(MethodSerializerView, generics.RetrieveUpdateDestroyAPIView):  
    """
    API: /<post_id>
    Methods: GET/PUT/PATCH
    """
    queryset = Post.objects.all()  
    method_serializer_classes = {
            ('GET', ): PostSerializer,
            ('PUT', 'PATCH'): PostSerializerWrite,
    }
    #serializer_class = PostSerializer


class CategoryList(generics.ListCreateAPIView):
    """
    API: /categories/
    Methods: GET/POST
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):  
    """
    API: /categories/<cat_id>
    Methods: GET/PUT/PATCH
    """
    queryset = Category.objects.all()  
    serializer_class = CategorySerializer


class AuthorList(generics.ListAPIView):
    """
    API: /authors/
    Methods: GET
    """
    queryset = User.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveAPIView):  
    """
    API: /authors/<author_id>
    Methods: GET
    """
    queryset = User.objects.all()  
    serializer_class = AuthorSerializer
