from abc import ABC, abstractmethod
from json import JSONDecodeError

from src.logger import timemethod
from src.datastructures import ServiceContext
from src.llm_configs import (
    LanguageModelConfig,
    LanguageModelNames,
    LanguageModelConfigRetriever,
)
from src.handlers import APIHandlerFactory


class AbstractLanguageModel(ABC):
    @abstractmethod
    def invoke(self, service_context: ServiceContext) -> ServiceContext:
        pass


class LanguageModel(AbstractLanguageModel):
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

    def __init__(self, config: LanguageModelConfig):
        self.config = config

    def invoke(self, service_context: ServiceContext) -> ServiceContext:
        return service_context


class OllamaLanguageModel(LanguageModel):
    """
    Documentation for LLama3_8B:
    The LLama3_8B class is an implementation of the LLM class that uses the LLaMA3 8B model.
    """

    def __init__(self, config: LanguageModelConfig):
        self.config = config
        self.api_handler = APIHandlerFactory().get_handler(config.model_provider)

    def invoke(self, service_context: ServiceContext) -> ServiceContext:
        # build the payload
        payload = self._build_payload(service_context)
        # make the request
        try:
            response = self.api_handler.post_request(
                self.config.api_url,
                payload,
            )
            service_context.response = response["response"]
        except JSONDecodeError:
            raise ValueError("Invalid JSON response")
        except Exception as e:
            raise e

        return service_context

    def _build_payload(self, service_context: ServiceContext) -> dict:
        payload = {
            "model": self.config.model_name,
            "prompt": service_context.parsed_query
            if service_context.parsed_query
            else service_context.input_query,
            "stream": True if self.config.options.get("stream") else False,
        }
        return payload


class AbstractLLMFactory(ABC):
    @abstractmethod
    def get_llm(self, model_name: LanguageModelNames) -> LanguageModel:
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

    def get_llm(self, model_name: LanguageModelNames) -> LanguageModel:
        if model_name == LanguageModelNames.LLAMA3_8B:
            config = LanguageModelConfigRetriever(model_name).get_config()
            return OllamaLanguageModel(config)
        if model_name == LanguageModelNames.MIXTRAL_7B:
            config = LanguageModelConfigRetriever(model_name).get_config()
            return OllamaLanguageModel(config)
        if model_name == LanguageModelNames.PHI3:
            config = LanguageModelConfigRetriever(model_name).get_config()
            return OllamaLanguageModel(config)
        else:
            raise ValueError(f"Invalid model name: {model_name}")
