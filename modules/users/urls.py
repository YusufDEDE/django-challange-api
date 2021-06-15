from .views import CreateUserView, MeUserView, SearchUserView
from django.urls import path, include

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('me/', MeUserView.as_view(), name='me'),
    path('search/', SearchUserView.as_view(), name='search')
]
