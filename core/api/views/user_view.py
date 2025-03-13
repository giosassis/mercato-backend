from rest_framework import status, viewsets
from rest_framework.response import Response
from core.services.user_service import UserService
from core.domain.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    def list(self, request):
        users = UserService.get_all_users()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = UserService.create_user(serializer.validated_data)
                return Response(
                    UserSerializer(user).data, status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            user = UserService.get_user_by_id(pk)
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            UserService.delete_user(pk)
            return Response(
                {"message": "User successfully deleted."},
                status=status.HTTP_204_NO_CONTENT,
            )
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
