from dataclasses import dataclass
from typing import Optional
from uuid import uuid4


@dataclass
class ServiceContext:
    """
    The service context is the main object we will use and modify in this program.
    At its very core, it holds the user input and the query response.
    """

    input_query: str
    input_arguments: dict
    parsed_query: Optional[str]
    response: str
    parsed_response: Optional[str]

    requires_llm: bool = True
    _context_id: str = str(uuid4())

    def __repr__(self):
        return f"ServiceContext(context_id={self._context_id}, user_input={self.input_query}, response={self.response}, parsed_response={self.parsed_response})"
