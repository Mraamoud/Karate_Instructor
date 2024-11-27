from django.urls import path
from .views import login_or_register_view, profile_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("sign/", login_or_register_view, name="signup"),
    path("profile/", profile_view, name='profile')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)