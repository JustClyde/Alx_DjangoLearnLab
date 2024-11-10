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
