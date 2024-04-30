from abc import ABC, abstractmethod
from argparse import ArgumentParser

from src.datastructures import ServiceContext


class AbstractParser(ABC):
    @abstractmethod
    def parse(self, service_context: ServiceContext) -> ServiceContext:
        pass


class InputArgumentParser(AbstractParser):
    """
    Documentation for InputArgumentParser:
    The InputArgumentParser class is an abstract class that defines the interface for parsing input arguments.
    The parse() method should be implemented by subclasses to parse the input arguments and return a ServiceContext object.

    Example:
    class MyInputParser(InputArgumentParser):
        def parse(self, service_context: ServiceContext) -> ServiceContext:
            return service_context

    my_input_parser = MyInputParser()
    service_context = my_input_parser.parse(service_context)
    print(service_context)
    """

    def __init__(self):
        self.parser = ArgumentParser()
        self.config = {
            "query": {
                "flags": ["query"],
                "kwargs": {"type": str, "nargs": "+", "help": "Input query string"},
            },
            "code": {
                "flags": ["-c", "--code"],
                "kwargs": {"action": "store_true", "help": "Code mode"},
            },
            "search": {
                "flags": ["-s", "--search"],
                "kwargs": {"action": "store_true", "help": "Search mode"},
            },
        }
        self._add_arguments()

    def parse(self, service_context: ServiceContext) -> ServiceContext:
        service_context.input_query = " ".join(self._parse_input_args()["query"])
        service_context.input_arguments = self._parse_input_args()
        return service_context

    def _add_arguments(self):
        for _, arg_config in self.config.items():
            self.parser.add_argument(*arg_config["flags"], **arg_config["kwargs"])

    def _parse_input_args(self) -> dict:
        return vars(self.parser.parse_args())


class QueryParser(AbstractParser):
    """
    Documentation for QueryParser:
    The QueryParser class is an abstract class that defines the interface for parsing user queries.
    The parse() method should be implemented by subclasses to parse the input query and return a UserInput object.

    Example:
    class MyQueryParser(QueryParser):
        def parse(self, query: str) -> UserInput:
            return UserInput(query=query)

    my_query_parser = MyQueryParser()
    user_input = my_query_parser.parse("hello world")
    print(user_input.query)  # Output: "hello world"
    """

    def __init__(self):
        pass

    def parse(self, service_context: ServiceContext) -> ServiceContext:
        return service_context


class AbstractResponseParser(ABC):
    @abstractmethod
    def parse(self, service_context: ServiceContext) -> ServiceContext:
        pass


class ResponseParser(AbstractParser):
    """
    Documentation for ResponseParser:
    The ResponseParser class is an abstract class that defines the interface for parsing query responses.
    The parse() method should be implemented by subclasses to parse the input query and return a QueryResponse object.

    Example:
    class MyResponseParser(ResponseParser):
        def parse(self, response: str) -> QueryResponse:
            return QueryResponse(response=response)

    my_response_parser = MyResponseParser()
    query_response = my_response_parser.parse("hello world")
    print(query_response.response)  # Output: "hello world"
    """

    def __init__(self):
        pass

    def parse(self, service_context: ServiceContext) -> ServiceContext:
        service_context.parsed_response = f"Tina: { service_context.response }"
        return service_context
