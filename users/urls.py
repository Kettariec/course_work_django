from django.urls import path
from users.apps import UsersConfig
from users.views import (UserLoginView, UserLogoutView, RegisterUserView,
                         verification, UserUpdateView, generate_password,
                         UserListView, status_user)

app_name = UsersConfig.name


urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(http_method_names = ['get', 'post', 'options']), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('verification/<str:code>/', verification, name='verification'),
    path('profile/genpassword', generate_password, name='genpassword'),
    path('profile/', UserUpdateView.as_view(), name='profile'),

    path('user_list/', UserListView.as_view(), name='user_list'),
    path('status_user/<int:pk>', status_user, name='status_user'),
]
