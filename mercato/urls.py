from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.api.views.sale_view import SaleViewSet
from core.api.views.fake_invoice_view import FakeInvoiceViewSet
from core.api.views.sale_item_view import SaleItemViewSet
from core.api.views.product_view import ProductViewSet
from core.api.views.category_view import CategoryViewSet
from core.api.views.payment_view import PaymentViewSet
from core.api.views.auth_view import LoginView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView
from core.api.views.user_view import UserViewSet


router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"sales", SaleViewSet, basename="sale")
router.register(r"users", UserViewSet, basename='user')
router.register(r"invoices", FakeInvoiceViewSet, basename='invoice')

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
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
