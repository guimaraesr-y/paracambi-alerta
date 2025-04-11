from paracambialerta.user.infra.repositories import DjangoUserRepository


class ListUsers:

    def __init__(self, user_repository=DjangoUserRepository()):
        self.repository = user_repository

    def execute(self):
        return self.repository.get_all()
