from rest_framework.response import Response
from rest_framework import viewsets

from paracambialerta.user.interface.serializers import UserInputSerializer
from paracambialerta.user.interface.serializers.user_serializer import UserOutputSerializer
from paracambialerta.user.use_cases.create_user import CreateUser
from paracambialerta.user.use_cases.list_users import ListUsers


class UserViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    def create(self, request):
        serializer = UserInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_data = serializer.to_dto()
        use_case = CreateUser()
        created_user = use_case.execute(user_data)

        output_serializer = UserOutputSerializer.from_dto(created_user)
        return Response(output_serializer.data)

    def list(self, request):
        output_serializer = UserOutputSerializer.from_dto(request.user)

        use_case = ListUsers()
        users_data = use_case.execute()

        output_serializer = UserOutputSerializer(users_data, many=True)
        return Response(output_serializer.data)
