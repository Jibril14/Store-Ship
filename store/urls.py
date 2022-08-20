from django.urls import path
from . import views
'''
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
'''
urlpatterns = [
    path('users/login/', views.UsersTokenObtainPairView.as_view(),
        name='login_pair_view'),
    path('users/profile/', views.user_profile, name='userprofile'),
    path('all/users/', views.all_users, name='all-users'),

  



    path('products/', views.index, name='index'),
]