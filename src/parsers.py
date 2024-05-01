from abc import ABC, abstractmethod
from argparse import ArgumentParser
from enum import StrEnum

from src.datastructures import ServiceContext


class InputArguments(StrEnum):
    QUERY = "query"
    CODE = "code"
    SEARCH = "search"
    VERBOSE = "verbose"


class AbstractParser(ABC):
    @abstractmethod
    def parse(self, context: ServiceContext) -> ServiceContext:
        pass


class InputArgumentParser:
    """
    Documentation for InputArgumentParser:
    This class defines the interface for parsing input arguments.
    The parse() method should be implemented by subclasses to parse the input arguments and return a ServiceContext object.
    """

    def __init__(self):
        self.parser = ArgumentParser(
            description="Parse input arguments for the application."
        )
        self.config = {
            InputArguments.QUERY: {
                "flags": ["query"],
                "kwargs": {"type": str, "nargs": "+", "help": "Input query string"},
            },
            InputArguments.CODE: {
                "flags": ["-c", "--code"],
                "kwargs": {"action": "store_true", "help": "Code mode"},
            },
            InputArguments.SEARCH: {
                "flags": ["-s", "--search"],
                "kwargs": {"action": "store_true", "help": "Search mode"},
            },
            InputArguments.VERBOSE: {
                "flags": ["-v", "--verbose"],
                "kwargs": {"action": "store_true", "help": "Output verbose logs"},
            },
        }
        self._add_arguments()

    def parse(self, context: ServiceContext) -> ServiceContext:
        args = self._parse_input_args()
        context.input_query = " ".join(args.get("query", []))
        context.input_arguments = args
        return context

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

    def parse(self, context: ServiceContext) -> ServiceContext:
        context.logger.info(f"Parsing input query: {context.input_query}")
        if context.input_arguments[InputArguments.CODE]:
            context.logger.info(f"Code mode detected")
            context.parsed_query = f"Help me with a question related to code. You should only return code and nothing else: { context.input_query }"
        # TODO: Execute an external action here: what is a scalable way to define this?
        elif context.input_arguments[InputArguments.SEARCH]:
            context.logger.info(f"Search mode detected")
            context.parsed_query = f"{ context.input_query }"
        else:
            context.logger.info(f"Default mode detected")
            context.parsed_query = f"{ context.input_query }"
        return context


class AbstractResponseParser(ABC):
    @abstractmethod
    def parse(self, context: ServiceContext) -> ServiceContext:
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

    def parse(self, context: ServiceContext) -> ServiceContext:
        context.parsed_response = f"Tina:\n{ context.response }"
        return context
