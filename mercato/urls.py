from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.api.views.sale_view import SaleViewSet
from core.api.views.sale_item_view import SaleItemViewSet
from core.api.views.product_view import ProductViewSet
from core.api.views.category_view import CategoryViewSet
from core.api.views.payment_view import PaymentViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"sales", SaleViewSet, basename="sale")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "products/category/<uuid:category_id>/",
        ProductViewSet.as_view({"get": "list_by_category"}),
        name="products-by-category",
    ),
    path(
        "sales/<uuid:sale_id>/items/",
        SaleItemViewSet.as_view({"get": "list", "post": "create"}),
        name="sale-items",
    ),
    path(
        "sales/items/<uuid:pk>/",
        SaleItemViewSet.as_view({"delete": "destroy"}),
        name="delete-sale-item",
    ),
    path(
        "sales/<uuid:sale_id>/payments/",
        PaymentViewSet.as_view({"get": "list", "post": "create"}),
        name="payments",
    ),
]
