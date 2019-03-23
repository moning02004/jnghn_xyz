from django.urls import path

from . import views


app_name = 'app_material'
urlpatterns = [
    path('', views.index_view, name="index"),
    path('new/', views.new_view, name="new"),
    path('detail/<int:pk>', views.detail_view, name="detail"),
    path('edit/<int:pk>', views.edit_view, name="edit"),
    path('__delete__/<int:pk>', views.delete, name="delete"),
    path('__delete__file__/<int:pk>/<int:file_id>', views.delete_file, name="delete_file"),
] 