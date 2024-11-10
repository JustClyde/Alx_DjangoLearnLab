from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view URL
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view URL
]
Step 
"views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="
from django.urls import path
from .views import register, user_login, user_logout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # Add your other URLs here
]
"add_book/", "edit_book/", "delete_book"
