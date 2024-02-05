from newsletter.forms import ClientForm, MessageForm, NewsLetterForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from newsletter.models import Client, NewsLetter, Message, Log
from django.views.generic import (CreateView, UpdateView,
                                  DeleteView, TemplateView, ListView)


class HomeTemplateView(TemplateView):
    """Контроллер главной страницы"""
    template_name = 'newsletter/index.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        client_count = len(Client.objects.filter(user=self.request.user.pk))
        message_count = len(Message.objects.filter(user=self.request.user.pk))
        newsletter_count = len(NewsLetter.objects.filter(user=self.request.user.pk))
        active_newsletter = len(NewsLetter.objects.filter(user=self.request.user.pk, status='started'))
        context_data['newsletter_count'] = newsletter_count
        context_data['client_count'] = client_count
        context_data['active_newsletter'] = active_newsletter
        context_data['message_count'] = message_count
        return context_data


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('newsletter:index')

    def form_valid(self, form):
        """Добавление пользователя к клиенту"""
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self):
        """Вывод клиентов пользователя"""
        return super().get_queryset().filter(user=self.request.user)


class ClientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('newsletter:client_list')

    def test_func(self):
        user = self.request.user
        if user == self.get_object().user:
            return True
        return self.handle_no_permission()


class ClientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('newsletter:client_list')

    def test_func(self):
        user = self.request.user
        if user == self.get_object().user:
            return True
        return self.handle_no_permission()


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('newsletter:index')

    def form_valid(self, form):
        """Добавление пользователя к сообщению"""
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_queryset(self):
        """Вывод сообщений пользователя"""
        return super().get_queryset().filter(user=self.request.user)


class MessageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('newsletter:message_list')

    def test_func(self):
        user = self.request.user
        if user == self.get_object().user:
            return True
        return self.handle_no_permission()


class MessageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('newsletter:message_list')

    def test_func(self):
        user = self.request.user
        if user == self.get_object().user:
            return True
        return self.handle_no_permission()


class NewsLetterCreateView(LoginRequiredMixin, CreateView):
    model = NewsLetter
    form_class = NewsLetterForm
    success_url = reverse_lazy('newsletter:index')

    def form_valid(self, form):
        """Добавление пользователя к рассылке"""
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class NewsLetterListView(LoginRequiredMixin, ListView):
    model = NewsLetter

    def get_queryset(self):
        """Вывод рассылок пользователя либо всех рассылок для модератора"""
        if self.request.user.has_perm('newsletter.view_newsletter'):
            return super().get_queryset()
        return super().get_queryset().filter(user=self.request.user)


class NewsLetterUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = NewsLetter
    form_class = NewsLetterForm
    success_url = reverse_lazy('newsletter:newsletter_list')

    def test_func(self):
        user = self.request.user
        if user == self.get_object().user:
            return True
        return self.handle_no_permission()


class NewsLetterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = NewsLetter
    success_url = reverse_lazy('newsletter:newsletter_list')

    def test_func(self):
        user = self.request.user
        if user == self.get_object().user:
            return True
        return self.handle_no_permission()


def status_newsletter(request, pk):
    """Контроллер смены статуса рассылки"""
    newsletter = NewsLetter.objects.get(pk=pk)
    if request.user == newsletter.user or request.user.has_perm('newsletter.set_status'):
        if newsletter.status == 'created':
            newsletter.status = 'started'
            newsletter.save()
        elif newsletter.status == 'started':
            newsletter.status = 'created'
            newsletter.save()
        else:
            newsletter.status = 'started'
            newsletter.save()
    return redirect(reverse('newsletter:newsletter_list'))


def finish_newsletter(request, pk):
    newsletter = NewsLetter.objects.get(pk=pk)
    if request.user == newsletter.user or request.user.has_perm('newsletter.set_status'):
        newsletter.status = 'completed'
        newsletter.save()
    return redirect(reverse('newsletter:newsletter_list'))


class LogListView(LoginRequiredMixin, ListView):
    model = Log

    def get_queryset(self):
        """Вывод сообщений пользователя"""
        return super().get_queryset().filter(user=self.request.user)
