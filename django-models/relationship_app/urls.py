from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view URL
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view URL
]
Step 
"views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="
