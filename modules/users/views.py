from .serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class CreateUserView(APIView):
    def get(self, request):
        return Response({
            'detail': 'SignUp not GET Method Allowed!',
            'status': status.HTTP_405_METHOD_NOT_ALLOWED
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                'detail': serializer.data,
                'status': status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeUserView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {
            'bio': list(Profile.objects.filter(user=request.user).values(
                'username', 'first_name', 'last_name', 'email', 'phone', 'about_us'
            )),
        }
        return Response(content)

    def put(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'detail': serializer.data,
                'status': status.HTTP_200_OK
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchUserView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        keyword = request.query_params.get('keyword')

        if keyword:
            return Response({
                'search_result': list(Profile.objects.filter(username__icontains=keyword).values(
                    'username', 'first_name', 'last_name', 'email', 'phone', 'about_us'
                ))
            })

        return Response({
            'error': 'Please correct query params! | /users/search?keyword=<keyword> ',
        })
