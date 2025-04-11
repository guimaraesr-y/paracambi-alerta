from paracambialerta.user.domain.dtos.create_user import CreateUserInput
from paracambialerta.user.domain.entities import User
from paracambialerta.user.infra.repositories import DjangoUserRepository


class CreateUser:

    def __init__(self, user_repository=DjangoUserRepository()):
        self.repository = user_repository

    def execute(self, user_data: CreateUserInput) -> User:
        new_user = User(**(user_data.__dict__))
        created_user = self.repository.save(new_user)
        return created_user
