from rest_framework import serializers

from paracambialerta.user.domain.dtos.create_user import CreateUserInput, CreateUserOutput


class UserInputSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def to_dto(self):
        return CreateUserInput(
            name=self.validated_data['username'],
            email=self.validated_data['email'],
            password=self.validated_data['password'],
        )


class UserOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)

    @classmethod
    def from_dto(cls, dto: CreateUserOutput):
        return cls(
            id=dto.id,
            name=dto.name,
            email=dto.email,
        )
