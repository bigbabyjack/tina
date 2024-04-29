from abc import ABC, abstractmethod

from src.datastructures import ServiceContext


class AbstractQueryParser(ABC):
    @abstractmethod
    def parse(self, service_context: ServiceContext) -> ServiceContext:
        pass


class QueryParser(AbstractQueryParser):
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


class ResponseParser(AbstractResponseParser):
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
        service_context.parsed_response = f"Response{ service_context.response }"
        return service_context
