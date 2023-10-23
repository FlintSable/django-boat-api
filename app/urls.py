from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('boats/', views.boat_list),
    path('slips/', views.slip_list)
]
