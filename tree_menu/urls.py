from django.urls import path

from . import views

app_name = 'tree_menu'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.menu, name='menu'),
]