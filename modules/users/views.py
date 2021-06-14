from .serializers import UserSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class MeUserView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {
            'me': list(User.objects.filter(username=request.user).values(
                'username',
                'first_name',
                'last_name',
            )),
        }
        return Response(content)


class SearchUserView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        keyword = request.query_params.get('keyword')

        if keyword:
            return Response({
                'search_result': list(User.objects.filter(username__icontains=keyword).values(
                    'username',
                    'first_name',
                    'last_name',
                ))
            })

        return Response({
            'error': 'Please correct query params! | /users/search?keyword=<keyword> ',
        })
