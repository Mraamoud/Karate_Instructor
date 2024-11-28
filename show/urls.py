from django.urls import path
from .views import HomeView, AboutView, ContactView, ProgramsView, TeamView , ProgressView
urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("about/", AboutView.as_view(), name='about'),
    path("contact/", ContactView.as_view(), name='contact'),
    path("programs/", ProgramsView.as_view(), name="programs"),
    path("team/", TeamView.as_view(), name="team"),
    path("progress/",ProgressView.as_view(), name="progress")
]