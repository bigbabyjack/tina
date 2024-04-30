from abc import ABC, abstractmethod

from src.datastructures import ServiceContext
from src.llms import LLMFactory, LanguageModelNames
from src.parsers import QueryParser, ResponseParser, InputArgumentParser
from src.executors import CommandExecutor


class AbstractOrchestrator(ABC):
    @abstractmethod
    def orchestrate(self) -> ServiceContext:
        pass


class LLMOrchestrator(AbstractOrchestrator):
    """
    Documentation for LLMOrchestrator:
    The LLMOrchestrator class is a class that orchestrates the query parsing, LLM invocation, and response parsing.
    It calls the QueryParser, LLMFactory, and ResponseParser to parse the query, invoke the LLM, and parse the response.

    """

    def __init__(self, service_context: ServiceContext, model_name: LanguageModelNames):
        self.model_name = model_name
        self.input_parser = InputArgumentParser()
        self.query_parser = QueryParser()
        self.llm = LLMFactory().get_llm(self.model_name)
        self.response_parser = ResponseParser()
        self.service_context = service_context

    def orchestrate(self) -> ServiceContext:
        try:
            self.service_context = self.input_parser.parse(self.service_context)
            self.service_context = self.query_parser.parse(self.service_context)
            if self.service_context.requires_llm:
                self.service_context = self.llm.invoke(self.service_context)
            else:
                self.command_executor = CommandExecutor().execute(self.service_context)
            self.service_context = self.response_parser.parse(self.service_context)
        except Exception as e:
            print(e)

        return self.service_context
