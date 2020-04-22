from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),
    path('blog/<slug>/',views.slug),
    path('login/',views.login),
    path('dashboard/',views.dashboard),
    path('dashboard/add',views.add),
    path('dashboard/delete',views.delete),
    path('dashboard/logout',views.logout),
]
