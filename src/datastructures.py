from dataclasses import dataclass


@dataclass
class UserInput:
    """ "
    The UserInput class contains data about the user's input.

    At it's most basic, it can hold just a query.
    """

    query: str


@dataclass
class QueryResponse:
    response: str


@dataclass
class ServiceContext:
    """
    The service context is the main object we will use and modify in this program.
    At its very core, it holds the user input and the query response.
    """

    user_input: UserInput
    query_response: QueryResponse
