from django.urls import path

from . import views

app_name = "app_portfolio"
urlpatterns = [
    path('', views.index_view, name="index"),
]
