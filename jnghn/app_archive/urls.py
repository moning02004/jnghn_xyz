from django.urls import path

from . import views


app_name = 'app_archive'
urlpatterns = [
    path('', views.index_view, name="index"),
    path('new/', views.new_view, name="new"),
    path('detail/<int:archive_id>', views.detail_view, name="detail"),
    path('edit/<int:archive_id>', views.edit_view, name="edit"),
    path('delete/<int:archive_id>', views.delete, name="delete"),
    path('delete_file/<int:archive_id>/<int:file_id>', views.delete_file, name="delete_file"),
] 