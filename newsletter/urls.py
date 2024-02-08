from newsletter.apps import NewsletterConfig
from django.urls import path
from newsletter.views import (HomeTemplateView, ClientListView, ClientUpdateView,
                              ClientDeleteView, MessageCreateView, MessageListView,
                              MessageUpdateView, MessageDeleteView, LogListView,
                              NewsLetterDeleteView, NewsLetterCreateView,
                              NewsLetterListView, NewsLetterUpdateView, ClientCreateView,
                              status_newsletter, finish_newsletter)


app_name = NewsletterConfig.name


urlpatterns = [
    path('', HomeTemplateView.as_view(), name='index'),

    path('create_client', ClientCreateView.as_view(), name='create_client'),
    path('client_list', ClientListView.as_view(), name='client_list'),
    path('edit_client/<int:pk>', ClientUpdateView.as_view(), name='edit_client'),
    path('delete_client/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),

    path('create_message', MessageCreateView.as_view(), name='create_message'),
    path('message_list', MessageListView.as_view(), name='message_list'),
    path('edit_message/<int:pk>', MessageUpdateView.as_view(), name='edit_message'),
    path('delete_message/<int:pk>', MessageDeleteView.as_view(), name='delete_message'),

    path('create_newsletter', NewsLetterCreateView.as_view(), name='create_newsletter'),
    path('newsletter_list', NewsLetterListView.as_view(), name='newsletter_list'),
    path('edit_newsletter/<int:pk>', NewsLetterUpdateView.as_view(), name='edit_newsletter'),
    path('delete_newsletter/<int:pk>', NewsLetterDeleteView.as_view(), name='delete_newsletter'),
    path('status_newsletter/<int:pk>', status_newsletter, name='status_newsletter'),
    path('finish_newsletter/<int:pk>', finish_newsletter, name='finish_newsletter'),

    path('log_list', LogListView.as_view(), name='log_list'),
]
