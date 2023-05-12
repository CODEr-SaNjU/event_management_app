from django.urls import path 
from event_app import views

urlpatterns = [
    path("", views.home_view, name="main_view")
]
