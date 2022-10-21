from django.urls import path

from accounts.views import signup, logout_user, login_user

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
]
