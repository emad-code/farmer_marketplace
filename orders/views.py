from rest_framework import generics, permissions
from rest_framework.response import Response
from decimal import Decimal

from .models import Order, OrderItem
from .serializers import OrderSerializer
from farms.models import Product


class CreateOrderView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        items = request.data.get("items", [])

        if not items:
            return Response({"error": "No items provided"}, status=400)

        total_price = Decimal("0.00")

        # Step 1: create order FIRST (we'll update total later)
        order = Order.objects.create(
            user=request.user,
            total_price=0
        )

        # Step 2: process items
        for item in items:
            try:
                product = Product.objects.get(id=item["product"])
            except Product.DoesNotExist:
                return Response(
                    {"error": f"Product {item['product']} not found"},
                    status=404
                )

            quantity = int(item["quantity"])
            item_price = product.price * quantity

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
            )

            total_price += item_price

        # Step 3: update total
        order.total_price = total_price
        order.save()

        return Response({
            "message": "Order created successfully",
            "order_id": order.id,
            "total_price": str(total_price)
        })
    

class OrderHistoryView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by("-created_at")