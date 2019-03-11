from django.urls import path

from . import views


app_name = 'app_notice'
urlpatterns = [
    path('', views.index_view, name="index"),
    path('new/', views.new_view, name="new"),
    path('_delete_/<int:notice_id>', views.delete, name="delete"),
]