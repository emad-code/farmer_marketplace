from django.urls import path
from .views import CreateOrderView, OrderHistoryView

urlpatterns = [
    path("create/", CreateOrderView.as_view()),
    path("", OrderHistoryView.as_view()),  # order history
]