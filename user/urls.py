from django.urls import path
from .views import login_or_register_view, ProfileView

urlpatterns = [
    path("sign/", login_or_register_view, name="signup"),
    path("profile/", ProfileView.as_view(), name='profile')
]