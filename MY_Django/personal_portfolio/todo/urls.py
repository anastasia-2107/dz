from django.urls import path
from . import views


urlpatterns = [
    # Auth (регистрация и авторизация)
    path('signup/', views.signup_user, name='signupuser'),
    path('logout/', views.logout_user, name='logoutuser'),
    path('login/', views.login_user, name='loginuser'),

    # Todos (постановка задач)
    path('current/', views.current_todos, name="currenttodos"),
    path('', views.home, name="home"),
]