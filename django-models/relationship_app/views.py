"views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="
"from django.views.generic.detail import DetailView"
"relationship_app/library_detail.html"
"relationship_app/list_books.html"
from django.shortcuts import render
from .models import Book  # Assuming you have a Book model 

def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'list_books.html', {'books': books})
  # relationship_app/views.py (continued)
from django.views.generic import DetailView
from .models import Library  # Assuming you have a Library model 

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # Specify your template name
    context_object_name = 'library'  # Default context variable to reference the object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Assuming a reverse relationship
        return context
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('some_view_name')  # Redirect to a success page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html', {})

# User Logout View
def user_logout(request):
    logout(request)
    return render(request, 'logout.html')
    "from django.contrib.auth import login", "from django.contrib.auth.forms import UserCreationForm"
    "views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="
    "from django.contrib.auth.decorators import permission_required", "relationship_app.can_add_book", "relationship_app.can_change_book", "relationship_app.can_delete_book"
    
