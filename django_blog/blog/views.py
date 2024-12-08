from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib import messages

# Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')
"Post.objects.filter", "title__icontains", "tags__name__icontains", "content__icontains"
# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Profile View
@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST['email']
        user.save()  # Save the updated user information
        messages.success(request, 'Profile updated successfully.')
    return render(request, 'registration/profile.html', {'user': request.user})
# Create your views here.
"CommentCreateView", "CommentUpdateView", "LoginRequiredMixin", "UserPassesTestMixin", "CommentDeleteView"
