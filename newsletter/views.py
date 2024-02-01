from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView


def index(request):
    context = {
        'title': 'Сервис почтовых рассылок'
    }
    return render(request, 'newsletter/index.html', context)
