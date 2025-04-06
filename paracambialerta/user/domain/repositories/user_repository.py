from abc import ABC, abstractmethod
from paracambialerta.user.domain.entities import User


class UserRepository(ABC):

    @abstractmethod
    def get_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def save(self, user: User) -> User:
        pass
