from abc import ABC, abstractmethod
from src.datastructures import UserInput, QueryResponse

from src.llm_configs import LLMConfig, LanguageModelNames, LLMConfigRetriever


class AbstractLLM(ABC):
    @abstractmethod
    def invoke(self, query: UserInput) -> QueryResponse:
        pass


class LLM(AbstractLLM):
    """
    Documentation for LLM:
    The LLM class is an abstract class that defines the interface for interacting with an LLM.

    Example:
    class MyLLM(LLM):
        def invoke(self, query: UserInput) -> QueryResponse:
            return QueryResponse(response="hello world")

    my_llm = MyLLM()
    query_response = my_llm.invoke(UserInput(query="hello world"))
    print(query_response.response)  # Output: "hello world"

    The invoke() method should be implemented by subclasses to interact with the LLM and return the response.
    """

    def __init__(self, config: LLMConfig):
        self.config = config

    def invoke(self, query: UserInput) -> QueryResponse:
        return QueryResponse(response="hello world")


class LLama3_8B(LLM):
    """
    Documentation for LLama3_8B:
    The LLama3_8B class is an implementation of the LLM class that uses the LLaMA3 8B model.
    """

    def __init__(self, config: LLMConfig):
        self.config = config

    def invoke(self, query: UserInput) -> QueryResponse:
        return QueryResponse(response="hello world")


class AbstractLLMFactory(ABC):
    @abstractmethod
    def get_llm(self, model_name: LanguageModelNames) -> LLM:
        pass


class LLMFactory(AbstractLLMFactory):
    """
    Documentation for LLMFactory:
    The LLMFactory class is an abstract class that defines the interface for creating LLMs.

    Example:
    class MyLLMFactory(LLMFactory):
        def get_llm(self, model_name: LLMAgents) -> LLM:
            if model_name == LLMAgents.LLAMA3_8B:
                config = LLMConfigRetriever(model_name).get_config()
                return LLama3_8B(config)
            else:
                raise ValueError(f"Invalid model name: {model_name}")

    my_llm_factory = MyLLMFactory()
    my_llm = my_llm_factory.get_llm(LLMAgents.LLAMA3_8B)

    The get_llm() method should be implemented by subclasses to return an instance of the LLM class.
    """

    def __init__(self):
        pass

    def __call__(self, model_name: LanguageModelNames) -> LLM:
        return self.get_llm(model_name)

    def get_llm(self, model_name: LanguageModelNames) -> LLM:
        if model_name == LanguageModelNames.LLAMA3_8B:
            config = LLMConfigRetriever(model_name).get_config()
            return LLama3_8B(config)
        else:
            raise ValueError(f"Invalid model name: {model_name}")
