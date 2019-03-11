from django.urls import path

from . import views


app_name = 'app_admin'
urlpatterns = [
    path('', views.index_view, name="index"),
    path('detail/<str:username>', views.detail_view, name="detail"),
    path('edit/<str:username>', views.edit_view, name="edit"),
    path('_delete_/<str:username>', views.delete_user, name="delete_user"),
    path('edit/', views.edit_me_view, name="edit_me"),

]