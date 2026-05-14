from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Создаём роутер
router = DefaultRouter()
router.register(r'posts', views.PostViewSet)        # /api/posts/
router.register(r'categories', views.CategoryViewSet)  # /api/categories/

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
    
    # ========== API маршруты (через Router) ==========
    path('api/', include(router.urls)),  # все API маршруты автоматически
]