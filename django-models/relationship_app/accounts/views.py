from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome Admin!")

@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome Librarian!")

@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome Member!")
