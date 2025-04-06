from dataclasses import dataclass


@dataclass
class CreateUserInput:
    name: str
    email: str
    password: str


@dataclass
class CreateUserOutput:
    id: int
    name: str
    email: str
