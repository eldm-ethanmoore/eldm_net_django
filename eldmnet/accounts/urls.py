from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('', views.home, name='index'),
    path('user_login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'), 
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]