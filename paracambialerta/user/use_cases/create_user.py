from paracambialerta.user.domain.entities import User
from paracambialerta.user.infra.repositories.django_user_repository import DjangoUserRepository


class CreateUser:

    def __init__(self, user_repository=DjangoUserRepository()):
        self.repository = user_repository

    def execute(self, user_data: dict) -> User:
        new_user = User(**user_data)
        created_user = self.repository.save(new_user)
        return created_user
