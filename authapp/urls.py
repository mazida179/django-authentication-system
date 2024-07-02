from django.urls import path
from .views import index, register_user, name_form
from .views.user import profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index.index, name='index'),
    path('register-user/', register_user.resigterUser, name='register-user'),

    path('name/', name_form.postName, name='name'),

    path('profile/', profile.userInfo, name='profile'),
]