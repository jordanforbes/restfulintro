from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('shows', views.index),
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('shows/<show_id>', views.show),
    path('shows/<show_id>/edit', views.edit),
    path('shows/<show_id>/update', views.update),
    path('shows/<show_id>/destroy', views.destroy)
]
