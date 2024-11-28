from django.urls import path
from . import views

urlpatterns = [
    path('progress/<int:user_id>/', views.user_progress, name='user_progress'),
]
