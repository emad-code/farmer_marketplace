from django.urls import path
from .views import (
    MyFarmView,
    MyProductsView,
    CreateProductView,
    UpdateProductView,
    DeleteProductView,
)

urlpatterns = [
    # FARM
    path("my-farm/", MyFarmView.as_view()),

    # PRODUCTS
    path("products/", MyProductsView.as_view()),
    path("products/create/", CreateProductView.as_view()),
    path("products/<int:pk>/update/", UpdateProductView.as_view()),
    path("products/<int:pk>/delete/", DeleteProductView.as_view()),
]
