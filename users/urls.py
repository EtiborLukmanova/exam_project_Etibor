from django.urls import path
from .views import HomepageView, ProfileView, UpdateProfileView, UserRegisterView, CustomUserLogin, CustomLogoutView

urlpatterns = [
    path('home/', HomepageView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update/', UpdateProfileView.as_view(), name='update_profile'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('', CustomUserLogin.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
