from .views import home, register, user_login, user_logout, user_profile
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
 
urlpatterns = [   
   path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('profile/', user_profile, name="profile"),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='appblog/password_reset.html'),
        name='password_reset',)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
