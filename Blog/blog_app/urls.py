from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),
    path('blog/<slug>/',views.slug),
    path('dashboard',views.dashboard),
]
