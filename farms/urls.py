from django.urls import path
from .views import MyFarmView, MyProductsView

urlpatterns = [
    path("my-farm/", MyFarmView.as_view()),
    path("my-products/", MyProductsView.as_view()),
]