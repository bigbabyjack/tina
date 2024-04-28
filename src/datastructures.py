from dataclasses import dataclass


@dataclass
class UserInput:
    query: str


@dataclass
class QueryResponse:
    response: str
