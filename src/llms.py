from abc import ABC, abstractmethod
from datastructures import UserInput, QueryResponse

from llm_configs import LLMConfig, LLMAgents


class AbstractLLM(ABC):
    @abstractmethod
    def invoke(self, query: UserInput, config: LLMConfig) -> QueryResponse:
        pass


class LLM(AbstractLLM):
    def invoke(self, query: UserInput, config: LLMConfig) -> QueryResponse:
        return QueryResponse(response="hello world")


class LLama3_8B(LLM):
    def invoke(self, query: UserInput, config: LLMConfig) -> QueryResponse:
        return QueryResponse(response="hello world")


class AbstractLLMFactory(ABC):
    @abstractmethod
    def get_llm(self) -> LLM:
        pass


class LLMFactory(AbstractLLMFactory):
    def __init__(self, model_name: LLMAgents):
        self.model_name = model_name

    def get_llm(self) -> LLM:
        if self.model_name == LLMAgents.LLAMA3_8B:
            return LLama3_8B()
        raise ValueError(f"Invalid model name: {self.model_name}")
