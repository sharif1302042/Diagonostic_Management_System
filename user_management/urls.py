from django.urls import path

from user_management import views

urlpatterns = [
    path('create/',views.UserCreate.as_view(), name='user/create'),
]
