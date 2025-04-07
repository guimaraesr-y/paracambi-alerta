from django.contrib.auth.models import User as DjangoUser

from misc.model_mapper import map_model_to_entity
from paracambialerta.user.domain.entities import User
from paracambialerta.user.domain.repositories import UserRepository


class DjangoUserRepository(UserRepository):

    def get_by_id(self, user_id: int) -> User:
        obj = DjangoUser.objects.get(pk=user_id)
        return map_model_to_entity(obj, User)

    def save(self, user: User) -> User:
        obj = DjangoUser.objects.create(**(user.__dict__))
        return map_model_to_entity(obj, User)
