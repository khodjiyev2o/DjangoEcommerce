from rest_framework.routers import DefaultRouter
from .veiwsets  import ProductViewSet,ProductGenericViewSet,CustomerGenericViewSet


router=DefaultRouter()
router.register('products-onlyList',ProductGenericViewSet,basename='products')
router.register('products-All',ProductViewSet,basename='productsss')
router.register('customers-onlyList',CustomerGenericViewSet,basename='customers')
urlpatterns = router.urls
print(urlpatterns)