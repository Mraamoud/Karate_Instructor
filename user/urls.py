from django.urls import path
from .views import login_or_register_view

urlpatterns = [
    path("sign/", login_or_register_view, name="signup"),
]