from dataclasses import dataclass


@dataclass
class CreateUserInput:
    first_name: str
    last_name: str
    username: str
    email: str
    password: str


@dataclass
class CreateUserOutput:
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
