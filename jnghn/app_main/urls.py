from django.urls import path
from . import views


app_name = 'app_main'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('search/', views.search_view, name="search"),
    path('site/', views.site_view, name='site'),
    path('password_check/<int:pk>', views.password_view, name='password_check'),
]
