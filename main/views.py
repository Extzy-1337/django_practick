from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm
from rest_framework.viewsets import ModelViewSet
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer

# ========== CBV для Post ==========

class PostListView(ListView):
    """Список всех постов (главная страница)"""
    model = Post
    template_name = 'main/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']  # сначала новые


class PostDetailView(DetailView):
    """Полный просмотр одного поста"""
    model = Post
    template_name = 'main/post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    """Создание нового поста"""
    model = Post
    form_class = PostForm
    template_name = 'main/post_form.html'
    success_url = reverse_lazy('post_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать пост'
        context['button_text'] = 'Создать'
        return context


class PostUpdateView(UpdateView):
    """Редактирование поста"""
    model = Post
    form_class = PostForm
    template_name = 'main/post_form.html'
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать пост'
        context['button_text'] = 'Сохранить'
        return context


class PostDeleteView(DeleteView):
    """Удаление поста"""
    model = Post
    template_name = 'main/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')


# ========== CBV для Category ==========

class CategoryListView(ListView):
    """Список категорий"""
    model = Category
    template_name = 'main/category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    """Создание категории"""
    model = Category
    fields = ['name']
    template_name = 'main/category_form.html'
    success_url = reverse_lazy('category_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать категорию'
        context['button_text'] = 'Создать'
        return context


class CategoryDeleteView(DeleteView):
    """Удаление категории"""
    model = Category
    template_name = 'main/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

# ========== API для постов ==========

class PostListAPIView(APIView):
    """API для получения списка постов и создания нового"""
    
    def get(self, request):
        """GET /api/posts/ — получить все посты"""
        posts = Post.objects.all().order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """POST /api/posts/ — создать новый пост"""
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailAPIView(APIView):
    """API для получения, обновления и удаления одного поста"""
    
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None
    
    def get(self, request, pk):
        """GET /api/posts/<id>/ — получить один пост"""
        post = self.get_object(pk)
        if not post:
            return Response({'error': 'Пост не найден'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, pk):
        """PUT /api/posts/<id>/ — полностью обновить пост"""
        post = self.get_object(pk)
        if not post:
            return Response({'error': 'Пост не найден'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """DELETE /api/posts/<id>/ — удалить пост"""
        post = self.get_object(pk)
        if not post:
            return Response({'error': 'Пост не найден'}, status=status.HTTP_404_NOT_FOUND)
        post.delete()
        return Response({'message': 'Пост удалён'}, status=status.HTTP_204_NO_CONTENT)
    
# ========== ViewSet для API ==========

class PostViewSet(ModelViewSet):
    """
    ViewSet для модели Post.
    Автоматически поддерживает: list, create, retrieve, update, partial_update, destroy
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer


class CategoryViewSet(ModelViewSet):
    """
    ViewSet для модели Category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer