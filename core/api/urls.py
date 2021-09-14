from django.urls import path
from .views import login, logout, signup, dashboard, stop_container

urlpatterns = [
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),
    path("logout/", logout, name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
    path("stop-container/", stop_container, name="stop-container"),
]
