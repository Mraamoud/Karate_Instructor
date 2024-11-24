from django.views.generic import TemplateView

class HomeView (TemplateView) :
    template_name = 'show/index.html'

class AboutView (TemplateView) :
    template_name = 'show/about.html'

class ContactView (TemplateView) :
    template_name = 'show/contact.html'

class ProgramsView (TemplateView) : 
    template_name = 'show/programs.html'

class TeamView (TemplateView) : 
    template_name = 'show/team.html'