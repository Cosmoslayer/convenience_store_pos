from django.urls import path

from api import views

urlpatterns = [
    path("categories", views.CategoryView.as_view()),
    path("items", views.ItemView.as_view()),
    path("items/<int:pk>", views.ItemDetailView.as_view()),
]
