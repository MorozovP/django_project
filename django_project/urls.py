from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('tree_menu.urls', namespace='menu')),
    path('admin/', admin.site.urls),
]