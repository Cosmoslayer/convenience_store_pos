from django.urls import path

from api import views

urlpatterns = [
    path("category", views.CategoryView.as_view()),
    path("item", views.ItemView.as_view()),
]
