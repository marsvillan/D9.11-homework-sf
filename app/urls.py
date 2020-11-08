from app.views import \
        PostList, PostDetail, \
        CategoryList, CategoryDetail, \
        AuthorList, AuthorDetail
from django.urls import path

app_name = 'app'
urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>', CategoryDetail.as_view(), name='category-detail'),
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>', AuthorDetail.as_view(), name='author-detail'),
]

