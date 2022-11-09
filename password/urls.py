from django.urls import path

from . import views

urlpatterns = [
    path('user', views.create_user),
    path('user/all', views.all_users),
    path('user/<int:id>', views.one_user),
    path('password', views.create_password)
]