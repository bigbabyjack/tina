from dataclasses import dataclass
from typing import Optional


@dataclass
class ServiceContext:
    """
    The service context is the main object we will use and modify in this program.
    At its very core, it holds the user input and the query response.
    """

    user_input: str
    response: str
    parsed_response: Optional[str]

    def __repr__(self):
        return f"ServiceContext(user_input={self.user_input}, response={self.response}, parsed_response={self.parsed_response})"
