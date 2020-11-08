from app.models import Post, Category
from rest_framework import serializers
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    """
    Сериализатор для Авторов (пользователей из _User_)
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для Категорий
    """
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializerNoPosts(serializers.ModelSerializer):
    """
    Сериализатор для Категорий без списка постов
    """
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор Постов для режимы вывода (GET)
    Будут отображаться все вложенные даные
    для _User_ и _Category_
    """
    author = AuthorSerializer()
    category = CategorySerializerNoPosts()
    class Meta:
        model = Post
        fields = '__all__'


class PostSerializerWrite(serializers.ModelSerializer):
    """
    Сериализатор Постов для режимы ввода (POST, PUT, PATCH)
    Для _User_ и _Category_ указываются только их id
    """
    class Meta:
        model = Post
        fields = '__all__'
