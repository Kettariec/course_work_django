from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import (CreateView, ListView,
                                  DetailView, UpdateView, DeleteView)
from blog.models import Blog
from blog.forms import BlogForm
from pytils.translit import slugify
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog

    def get_queryset(self):
        """Вывод постов пользователя"""
        return super().get_queryset().filter(user=self.request.user)


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')


def toggle_activity(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.is_published:
        blog_item.is_published = False
    else:
        blog_item.is_published = True
    blog_item.save()
    return redirect(reverse('blog:list'))
