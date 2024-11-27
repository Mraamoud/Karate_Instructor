from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, LoginForm, UpdateProfileForm, UpdateUserInfoForm
from .models import Profile

def login_or_register_view(request):
    signup_form = SignUpForm()
    login_form = LoginForm()
    if request.method == "POST":
        if 'signup' in request.POST:  # Check which form was submitted
            signup_form = SignUpForm(request.POST)
            login_form = LoginForm()
            if signup_form.is_valid():
                # Create the user
                user = signup_form.save(commit=False)
                user.set_password(signup_form.cleaned_data['password'])
                user.save()
                # Automatically log the user in after sign-up
                login(request, user)
                return redirect('home')  # Redirect to home or dashboard
        elif 'signin' in request.POST:
            login_form = LoginForm(request, data=request.POST)
            signup_form = SignUpForm()
            if login_form.is_valid():
                # Authenticate and log the user in
                user = authenticate(username=login_form.cleaned_data['username'], 
                                    password=login_form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('home')  # Redirect to home or dashboard
                else : 
                    login_form.add_error(None, "Invalid email or password")
    return render(request, 'user/SignUp.html', {'signup_form': signup_form, 'login_form': login_form})

@login_required
def profile_view (request) :
    user = request.user
    profile_form = UpdateProfileForm(instance=user.profile)
    user_info_form = UpdateUserInfoForm(instance=user)
    if request.method == "POST" :
        if "general-change" in request.POST :
            user_info_form = UpdateUserInfoForm(request.POST, instance=user)
            profile_form = UpdateProfileForm(request.POST, request.FILES, instance=user.profile)
            if user_info_form.is_valid() and profile_form.is_valid() :
                user_info_form.save()
                profile_form.save()
                return redirect('profile')
        elif "password-changed" in request.POST : 
            user_info_form = UpdateUserInfoForm(request.POST, instance=user)
            if user_info_form.is_valid() :
                user_info_form.save()
                return redirect('profile')
    return render(request=request, template_name="user/profile.html", 
                context={"profile_form" : profile_form, "user_info_form" : user_info_form})