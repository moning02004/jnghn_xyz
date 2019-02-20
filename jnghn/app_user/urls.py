from django.urls import path

from . import views


app_name = "app_user"
urlpatterns = [
    path('', views.index_view, name="index"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('profile/', views.profile_view, name="profile"),
    path('edit/', views.edit_view, name="edit"),
    path('find/', views.find_view, name="find"),
    path('reset/', views.reset_view, name="reset"),
    path('logout/', views.logout, name="logout"),
    path('leave/<str:username>/', views.leave, name="leave"),
]