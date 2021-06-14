from rest_framework.routers import DefaultRouter
from .views import CreateUserView, MeUserView
from django.urls import path, include

router = DefaultRouter()
router.register(r'signup', CreateUserView, basename='signup/')

urlpatterns = router.urls

urlpatterns += [
    path('me/', MeUserView.as_view(), name='ex')
]
