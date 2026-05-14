from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm


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