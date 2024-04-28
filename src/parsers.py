from abc import ABC, abstractmethod

from datastructures import UserInput, QueryResponse


class AbstractQueryParser(ABC):
    @abstractmethod
    def parse(self, query: str) -> UserInput:
        pass


class QueryParser(AbstractQueryParser):
    def parse(self, query: str) -> UserInput:
        return UserInput(query=query)


class AbstractResponseParser(ABC):
    @abstractmethod
    def parse(self, response: str) -> QueryResponse:
        pass


class ResponseParser(AbstractResponseParser):
    def parse(self, response: str) -> QueryResponse:
        return QueryResponse(response=response)
