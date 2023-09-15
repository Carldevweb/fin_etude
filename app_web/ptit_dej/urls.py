from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('victim/', views.victim, name='victim'),
    
    path('account/', views.account, name='account'),
    
    path('palmeOr/', views.palmeOr, name='palmeOr'),
    path('palmeDej/', views.palmeDej,name='palmeDej'),
    path('useFlag/', views.useFlag, name='useFlag'),
    path('team/', views.team, name='team'),
    path('offrandes/', views.offrandes, name='offrandes'),
    
    # API endpoint
    path('api/consomables', views.consomables, name='consomables'),
    path('api/attack', views.attack, name='attack'),
    path('api/attack2', views.attack2, name='flag_attack'),
    path('api/login', views.login_app, name='login_app'),       
]