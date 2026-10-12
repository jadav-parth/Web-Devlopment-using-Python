from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# 1. Sign Up View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'authapp/register.html', {'form': form})

# 2. Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard_url')
    else:
        form = AuthenticationForm()
    return render(request, 'authapp/login.html', {'form': form})

# 3. Dashboard / Home View (Protected)
def dashboard_view(request):
    return render(request, 'authapp/dashboard.html')

# 4. Logout View
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login_url')
    return render(request, 'authapp/logout.html')