from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.api.views.product_view import ProductViewSet
from core.api.views.category_view import CategoryViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
    path('products/category/<uuid:category_id>/', ProductViewSet.as_view({'get': 'list_by_category'}), name='products-by-category'),
]