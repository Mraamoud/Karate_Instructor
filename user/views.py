from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .forms import SignUpForm, LoginForm
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
def profile_view(request):
    user = request.user
    profile = user.profile

    if request.method == "POST":
        if "general-change" in request.POST:
            errors = []
            new_username = request.POST.get("Username")
            if new_username:
                user.username = new_username

            new_email = request.POST.get("Email")
            if new_email:
                if new_email != user.email:
                    try:
                        validate_email(new_email)
                    except ValidationError:
                        errors.append("Invalid email format.")
                    if User.objects.filter(email=new_email).exists():
                        errors.append("This email is already in use.")
                    else : 
                        user.email = new_email

            new_profile_image = request.FILES.get("profile-image")
            if new_profile_image:
                allowed_file_types = ["image/jpeg", "image/png", "image/gif"]
                if new_profile_image.content_type not in allowed_file_types:
                    errors.append("Invalid image type. Only JPEG, PNG, and GIF are allowed.")

            if errors:
                return render(request, "user/profile.html", { "errors": errors })

            if new_profile_image:
                if profile.profile_image and profile.profile_image.name != "profile_pics/default.png":
                    profile.profile_image.delete(save=False)
                profile.profile_image = new_profile_image

            user.save()
            profile.save()
            return redirect("profile")

        elif "password-changed" in request.POST:
            current_password = request.POST["current_password"]
            new_password = request.POST["new_password"]
            confirm_password = request.POST["confirm_password"]
            if (current_password and new_password and (check_password(current_password, user.password)) and (new_password == confirm_password)) :
                user.set_password(new_password)
                user.save()
                return redirect("profile")

    return render(request, "user/profile.html")
