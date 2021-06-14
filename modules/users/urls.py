from rest_framework.routers import DefaultRouter
from .views import CreateUserView

router = DefaultRouter()
router.register(r'signup', CreateUserView)

urlpatterns = router.urls
