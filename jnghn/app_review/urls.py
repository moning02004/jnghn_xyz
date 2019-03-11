from django.urls import path

from . import views


app_name = "app_review"
urlpatterns = [
    path('', views.index_view, name="index"),
    path('detail/<int:review_id>', views.detail_view, name="detail"),
    path('edit/<int:review_id>', views.edit_view, name="edit"),
    path('_delete_/<int:review_id>', views.delete, name="delete"),
    path('new/<int:plan_id>', views.new_view, name="new"),
    path('_delete_content_/<int:review_id>/<int:file_id>', views.delete_content, name="delete_content"),
]