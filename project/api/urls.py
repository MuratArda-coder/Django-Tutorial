from rest_framework.routers import SimpleRouter
from .views import postViewSet

router = SimpleRouter()
router.register('posts',postViewSet)

urlpatterns = router.urls