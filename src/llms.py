from abc import ABC, abstractmethod

from datastructures import UserInput, QueryResponse


class AbstractLLM(ABC):
    @abstractmethod
    def respond(self, query: UserInput) -> QueryResponse:
        pass
