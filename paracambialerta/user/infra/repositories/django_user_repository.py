from django.contrib.auth.models import User as DjangoUser

from misc.model_mapper import map_model_to_entity
from paracambialerta.user.domain.entities import User
from paracambialerta.user.domain.repositories import UserRepository


class DjangoUserRepository(UserRepository):

    def get_by_id(self, user_id: int) -> User:
        obj = DjangoUser.objects.get(pk=user_id)
        return map_model_to_entity(obj, User)

    def get_all(self):
        objs = DjangoUser.objects.all()
        return [map_model_to_entity(obj, User) for obj in objs]

    def save(self, user: User) -> User:
        obj = DjangoUser.objects.create(**(user.__dict__))
        return map_model_to_entity(obj, User)

    def update(self, user: User) -> User:
        obj = DjangoUser.objects.get(pk=user.id)
        obj.first_name = user.first_name
        obj.last_name = user.last_name
        obj.save()
        return map_model_to_entity(obj, User)

    def delete(self, user_id: int):
        obj = DjangoUser.objects.get(pk=user_id)
        obj.delete()
