from django.urls import path

from . import views

app_name = "app_plan"
urlpatterns = [
    path('', views.index_view, name="index"),
    path('detail/<int:pk>/', views.detail_view, name="detail"),
    path('check/<int:pk>/', views.password_check, name="password_check"),
    path('edit/<int:pk>/', views.edit_view, name="edit"),
    path('_delete_/<int:pk>/', views.delete, name="delete"),
    path('new/<int:period>/', views.new_view, name="new"),
    path('type/', views.router_view, name="router"),
    path('_finish__/<int:pk>/', views.finish, name="complete"),
    path('_delete__/<int:pk>/<int:day_id>/<int:detail_id>/', views.delete_detail, name="delete_detail"),
]









