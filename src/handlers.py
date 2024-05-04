from abc import ABC, abstractmethod
import requests
from enum import StrEnum

from src.llm_configs import LanguageModelProviders
from src.logger import timemethod


class HandlerNames(StrEnum):
    API = "api"
    OLLAMA = "ollama"


class AbstractAPIHandler(ABC):
    @abstractmethod
    def post_request(self, api_url: str, payload: dict) -> dict:
        pass


class BaseAPIHandler(AbstractAPIHandler):
    @timemethod
    def post_request(self, api_url: str, payload: dict) -> dict:
        response = requests.post(url=api_url, json=payload)
        response.raise_for_status()
        response = response.json()
        return response


class OllamaAPIHandler(BaseAPIHandler):
    def __init__(self):
        super().__init__()

    @timemethod
    def post_request(self, api_url: str, payload: dict) -> dict:
        self._validate_payload(payload)
        response = requests.post(url=api_url, json=payload)
        response.raise_for_status()
        response = response.json()
        return response

    def _validate_payload(self, payload: dict) -> None:
        if not isinstance(payload, dict):
            raise ValueError(f"Invalid payload: {payload}")


class AbstractHandlerFactory(ABC):
    @abstractmethod
    def get_handler(self, model_provider: LanguageModelProviders) -> AbstractAPIHandler:
        pass


class APIHandlerFactory(AbstractHandlerFactory):
    def get_handler(self, model_provider: LanguageModelProviders) -> AbstractAPIHandler:
        if model_provider == LanguageModelProviders.OLLAMA:
            return OllamaAPIHandler()
        else:
            raise ValueError(f"Invalid handler name: {model_provider}")
