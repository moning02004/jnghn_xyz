from django.urls import path
from . import views


app_name = 'app_coffee'
urlpatterns = [
    path('beans/', views.beans_index, name="beans"),
    path('beans/new/', views.beans_new, name="beans_new"),
    path('beans/edit/<int:pk>/', views.beans_edit, name="beans_edit"),
    path('community/', views.community_index, name="community"),
    path('community/new/', views.community_new, name="community_new"),
    path('community/edit/<int:pk>/', views.community_edit, name="community_edit"),
    path('community/detail/<int:pk>/', views.community_detail, name="community_detail"),
    path('account/', views.account_index, name="account"),
    path('account/new/', views.account_new, name="account_new"),
    path('account/renew/<int:pk>/', views.account_renew, name="account_renew")
]
