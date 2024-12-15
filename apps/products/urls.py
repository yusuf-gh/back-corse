from django.urls import path
from .views import *

urlpatterns = [
    path("products/", ProductViewGET.as_view(), name="product-list"),
    path("product/<int:id>/", ProductViewGetSingle.as_view(), name="product-detail"),
    path("product/create/", ProductViewPOST.as_view(), name="add-new-product"),
    path("product/<int:id>/update/", ProductViewPutPatch.as_view(), name="product-update"),
    path("product/<int:id>/delete/", ProductViewDELETE.as_view(), name="delete-product")

]