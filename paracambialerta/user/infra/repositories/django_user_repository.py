from django.contrib.auth.models import User as DjangoUser

from paracambialerta.user.domain.entities import User
from paracambialerta.user.domain.repositories import UserRepository


class DjangoUserRepository(UserRepository):

    def get_by_id(self, user_id: int) -> User:
        obj = DjangoUser.objects.get(pk=user_id)
        return User(id=obj.id, name=obj.name, email=obj.email)

    def save(self, user: User) -> User:
        obj = DjangoUser.objects.create(name=user.name, email=user.email)
        return User(id=obj.id, name=obj.name, email=obj.email)
