from abc import ABC, abstractmethod
import requests
from enum import StrEnum


class HandlerNames(StrEnum):
    API = "api"
    LLAMA = "llama"


class AbstractAPIHandler(ABC):
    @abstractmethod
    def post_request(self, api_url: str, payload: dict) -> dict:
        pass


class BaseAPIHandler(AbstractAPIHandler):
    def post_request(self, api_url: str, payload: dict) -> dict:
        response = requests.post(url=api_url, json=payload)
        response.raise_for_status()
        response = response.json()
        return response


class LlamaAPIHandler(BaseAPIHandler):
    def __init__(self):
        super().__init__()

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
    def get_handler(self, handler_name: str) -> AbstractAPIHandler:
        pass


class APIHandlerFactory(AbstractHandlerFactory):
    def get_handler(self, handler_name: str) -> AbstractAPIHandler:
        if handler_name == HandlerNames.API:
            return BaseAPIHandler()
        elif handler_name == HandlerNames.LLAMA:
            return LlamaAPIHandler()
        else:
            raise ValueError(f"Invalid handler name: {handler_name}")
