from django.urls import path

from . import views


app_name = "app_user"
urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('__check__/', views.check_username, name="check"),
    path('profile/', views.profile_view, name="profile"),
    path('edit/', views.edit_view, name="edit"),
    path('find/', views.find_view, name="find"),
    path('reset/', views.reset_view, name="reset"),
    path('__logout__/', views.logout, name="logout"),
    path('__leave__/<str:username>/', views.leave, name="leave"),
]