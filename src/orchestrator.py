from abc import ABC, abstractmethod

from src.datastructures import QueryResponse
from src.llms import LLMFactory, LanguageModelNames
from src.parsers import QueryParser, ResponseParser


class AbstractOrchestrator(ABC):
    @abstractmethod
    def orchestrate(self, query: str) -> QueryResponse:
        pass


class LLMOrchestrator(AbstractOrchestrator):
    def __init__(self, model_name: LanguageModelNames):
        self.model_name = model_name
        self.query_parser = QueryParser()
        self.llm = LLMFactory().get_llm(llm_model_name)
        self.response_parser = ResponseParser()

    def orchestrate(self, query: str) -> QueryResponse:
        # Parse the query
        user_input = self.query_parser.parse(query)
        response = self.llm.invoke(user_input)

        return query_response
