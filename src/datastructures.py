from dataclasses import dataclass
from typing import Optional
from uuid import uuid4


@dataclass
class ServiceContext:
    """
    The service context is the main object we will use and modify in this program.
    At its very core, it holds the user input and the query response.
    """

    user_input: str
    parsed_query: Optional[str]
    response: str
    parsed_response: Optional[str]

    _context_id: str = str(uuid4())

    def __repr__(self):
        return f"ServiceContext(context_id={self._context_id}, user_input={self.user_input}, response={self.response}, parsed_response={self.parsed_response})"
