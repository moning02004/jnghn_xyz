from django.urls import path

from . import views


app_name = 'app_freetalk'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('detail/<int:pk>/', views.detail_view, name='detail'),
    path('new/', views.new_view, name='new'),
]