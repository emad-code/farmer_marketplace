from django.urls import path
from .views import (
    MyFarmView,
    MyProductsView,
    CreateProductView,
    UpdateProductView,
    DeleteProductView,
    PublicFarmListView,
    FarmProductsView,
    AllProductsView
)

urlpatterns = [
    # FARM
    path("my-farm/", MyFarmView.as_view()),

    # PRODUCTS
    path("products/", MyProductsView.as_view()),
    path("products/create/", CreateProductView.as_view()),
    path("products/<int:pk>/update/", UpdateProductView.as_view()),
    path("products/<int:pk>/delete/", DeleteProductView.as_view()),

    # PUBLIC MARKETPLACE
    path("farms/", PublicFarmListView.as_view()),
    path("farms/<int:farm_id>/products/", FarmProductsView.as_view()),
    path("products/all/", AllProductsView.as_view()),
]
