from abc import ABC, abstractmethod
from datastructures import UserInput, QueryResponse

from llm_configs import LLMConfig, LLMAgents, LLMConfigRetriever


class AbstractLLM(ABC):
    @abstractmethod
    def invoke(self, query: UserInput) -> QueryResponse:
        pass


class LLM(AbstractLLM):
    def __init__(self, config: LLMConfig):
        self.config = config

    def invoke(self, query: UserInput) -> QueryResponse:
        return QueryResponse(response="hello world")


class LLama3_8B(LLM):
    def __init__(self, config: LLMConfig):
        self.config = config

    def invoke(self, query: UserInput) -> QueryResponse:
        return QueryResponse(response="hello world")


class AbstractLLMFactory(ABC):
    @abstractmethod
    def get_llm(self, model_name: LLMAgents) -> LLM:
        pass


class LLMFactory(AbstractLLMFactory):
    def get_llm(self, model_name: LLMAgents) -> LLM:
        if model_name == LLMAgents.LLAMA3_8B:
            config = LLMConfigRetriever(model_name).get_config()
            return LLama3_8B(config)
        else:
            raise ValueError(f"Invalid model name: {model_name}")
