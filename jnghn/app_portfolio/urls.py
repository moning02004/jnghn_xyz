from django.urls import path

from . import views

app_name = "app_portfolio"
urlpatterns = [
    path('', views.index_view, name="index"),
    path('detail/<int:pk>/', views.detail_view, name="detail"),
    path('new/', views.new_view, name="new"),
    path('edit/<int:pk>/', views.edit_view, name="edit"),
    path('delete/<int:pk>/', views.delete, name="delete"),
]
