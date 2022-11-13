from django.urls import path

from core import views

urlpatterns = [
    path('', views.ContactView.as_view(), name="contact")
]