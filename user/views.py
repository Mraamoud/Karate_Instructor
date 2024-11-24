from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
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
    else:
        pass
    return render(request, 'user/SignUp.html', {'signup_form': signup_form, 'login_form': login_form})
