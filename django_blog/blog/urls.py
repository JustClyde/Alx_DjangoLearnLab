from django.urls import path
from .views import register, login_view, logout_view, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
]
"comment/<int:pk>/update/", "post/<int:pk>/comments/new/", "comment/<int:pk>/delete/"
"tags/<slug:tag_slug>/", "PostByTagListView.as_view()"
