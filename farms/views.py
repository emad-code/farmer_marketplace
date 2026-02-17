from rest_framework import generics, permissions
from .models import Farm, Product
from .serializers import FarmSerializer, ProductSerializer
from .permissions import IsProductOwner
from rest_framework.permissions import AllowAny


# Create your views here.

## FARMER APIs - PRIVATE

class MyFarmView(generics.ListCreateAPIView):
    serializer_class = FarmSerializer
    permission_classes = [permissions.IsAuthenticated]

    # LIST farms
    def get_queryset(self):
        return Farm.objects.filter(owner=self.request.user)

    # CREATE farms
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# LIST — Get all products belonging to logged-in farmer
class MyProductsView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(farm__owner=self.request.user)

# CREATE — Add product to your farm
class CreateProductView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        farm = Farm.objects.filter(owner=self.request.user).first()
        serializer.save(farm=farm)


# UPDATE — Edit your product
class UpdateProductView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsProductOwner]
    queryset = Product.objects.all()


# DELETE — Remove product
class DeleteProductView(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsProductOwner]
    queryset = Product.objects.all()


## CUSTOMER APIs - PUBLIC

# PUBLIC: List all farms
class PublicFarmListView(generics.ListAPIView):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [AllowAny]


# PUBLIC: List products of a specific farm
class FarmProductsView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        farm_id = self.kwargs["farm_id"]
        return Product.objects.filter(farm_id=farm_id)


# PUBLIC: List all products in marketplace
class AllProductsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]