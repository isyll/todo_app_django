from django.urls import path
from .views import TodosViews

urlpatterns = [path("test/", TodosViews.handleTest)]
