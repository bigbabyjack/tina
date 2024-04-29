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
        self.llm = LLMFactory().get_llm(self.model_name)
        self.response_parser = ResponseParser()

    def orchestrate(self, query: str) -> QueryResponse:
        # Parse the query
        # this returns a UserInput object
        user_input = self.query_parser.parse(query)

        # Invoke the LLM and get a QueryResponse object
        llm_response = self.llm.invoke(user_input)

        # Parse the response
        parsed_response = self.response_parser.parse(llm_response.response)

        return parsed_response
