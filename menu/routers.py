from rest_framework.routers import DefaultRouter
from .veiwsets  import ProductViewSet,ProductGenericViewSet


router=DefaultRouter()
router.register('products-onlyList',ProductGenericViewSet,basename='products')
router.register('products-All',ProductViewSet,basename='productsss')

urlpatterns = router.urls
print(urlpatterns)