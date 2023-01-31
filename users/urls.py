
from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path ('login/', views.login_view , name = 'login'),
    path ('logout/' , LogoutView.as_view(template_name = 'users/logout.html')),
    path ('register/' ,  views.register , name = 'register'),
    path('update/', views.update_user, name = 'update_user'),
    path ('update_user_profile/' , views.update_user_profile)
]



