from dataclasses import dataclass


@dataclass
class UserInput:
    query: str


@dataclass
class QueryResponse:
    response: str


@dataclass
class ServiceContext:
    user_input: UserInput
    query_response: QueryResponse
