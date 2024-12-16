from django.urls import path
from .views import *

urlpatterns = [
    path("products/", ProductViewGET.as_view(), name="product-list"),
    path("product/<uuid:pk>/", ProductViewGetSingle.as_view(), name="product-detail"),
    # path("product/create/", ProductViewPOST.as_view(), name="add-new-product"),
    path("product/<uuid:pk>/update/", ProductViewPutPatch.as_view(), name="product-update"),
    path("product/<uuid:pk>/delete/", ProductViewDELETE.as_view(), name="delete-product")

]