from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.CreateUser.as_view(), name='user-create'),
    path('<int:pk>/',   views.UpdateUser.as_view(), name='user-update'),
]