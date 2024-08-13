from django.urls import path
from users import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("signup", views.signupView, name="signup"),
    path("login", views.loginView, name="login"),
    path("logout", views.logoutView, name="logout"),
]