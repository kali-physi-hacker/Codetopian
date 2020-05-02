from django.urls import path
from django.contrib.auth import views
from .views import UserViewSet, UserRegister

urlpatterns = [
    path('login/', UserViewSet.as_view(), name="accounts"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('registers/', UserRegister, name="register"),
]