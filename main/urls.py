from django.urls import path
from . import views

urlpatterns = [
    # WEB маршруты (для браузера)
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    
    # Маршруты для категорий (WEB)
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    
    # ========== API маршруты ==========
    path('api/posts/', views.PostListAPIView.as_view(), name='api_posts'),
    path('api/posts/<int:pk>/', views.PostDetailAPIView.as_view(), name='api_post_detail'),
]