from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductViewGET(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductViewGetSingle(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# class ProductViewPOST(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class ProductViewPutPatch(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductViewDELETE(generics.DestroyAPIView):
    queryset = Product.objects.all()


