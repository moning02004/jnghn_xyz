from django.urls import path

from . import views


app_name = 'app_admin'
urlpatterns = [
    path('', views.index_view, name="index"),
    path('detail/<str:username>', views.detail_view, name="detail"),
    path('edit/<str:username>', views.edit_view, name="edit"),
    path('delete/<str:username>', views.delete_user, name="delete_user"),
    path('delete_plan', views.delete_plan, name="delete_plan"),
    path('delete_gallery', views.delete_gallery, name="delete_gallery"),
    path('delete_archive', views.delete_archive, name="delete_archive"),

]