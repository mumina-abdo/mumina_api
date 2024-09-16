# from django.urls import path

# from . import views

# urlpatterns = [
#     path("", views.index, name='index'),
#     path('login/', views.auth_login_view, name='login'),
#     path("logout/", views.logout, name='logout'),
#     path("callback/", views.callback, name='callback'),
#     path("register/", views.register, name='register'),
    
# ]





from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('callback/', views.callback, name='callback'),
    path('logout/', views.logout, name='logout'),
]
