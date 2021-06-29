from django.urls import path

from notes.profile_app.views import profile_info, create_profile, delete_profile

urlpatterns = [
    path('profile/', profile_info, name='profile info'),
    path('create/', create_profile, name='create profile'),
    path('profile/delete/', delete_profile, name= 'delete profile'),
]