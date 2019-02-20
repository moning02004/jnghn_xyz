from django.urls import path

from . import views

app_name = "app_plan"
urlpatterns = [
    path('', views.index_view, name="index"),
    path('detail/<int:pk>/', views.detail_view, name="detail"),
    path('edit/<int:pk>/', views.edit_view, name="edit"),
    path('delete/<int:pk>/', views.delete, name="delete"),
    path('delete_plan/<int:pk>/<int:detail_id>/', views.delete_plan, name="delete_plan"),
    path('new/<int:period>/', views.new_view, name="new"),
    path('type/', views.router_view, name="router"),
    path('finish/<int:pk>/', views.finish, name="complete"),
]









