from paracambialerta.user.infra.repositories.django_user_repository import DjangoUserRepository


class ListUsers:

    def __init__(self, user_repository=DjangoUserRepository()):
        self.repository = user_repository

    def execute(self):
        return self.repository.get_all()
