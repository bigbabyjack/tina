from abc import ABC, abstractmethod
import requests
from requests import Response
from enum import StrEnum


class HandlerNames(StrEnum):
    API = "api"
    LLAMA = "llama"


class AbstractHandler(ABC):
    @abstractmethod
    def post_request(self, api_url: str, payload: dict) -> Response:
        pass


class APIHandler(AbstractHandler):
    def post_request(self, api_url: str, payload: dict) -> Response:
        response = requests.post(api_url, json=payload)
        return response


class LlamaAPIHandler(APIHandler):
    def __init__(self):
        super().__init__()

    def post_request(self, api_url: str, payload: dict) -> Response:
        self._validate_payload(payload)
        response = requests.post(api_url, json=payload)
        return response

    def _validate_payload(self, payload: dict) -> None:
        if not isinstance(payload, dict):
            raise ValueError(f"Invalid payload: {payload}")


class AbstractHandlerFactory(ABC):
    @abstractmethod
    def get_handler(self, handler_name: str) -> AbstractHandler:
        pass


class APIHandlerFactory(AbstractHandlerFactory):
    def get_handler(self, handler_name: str) -> AbstractHandler:
        if handler_name == HandlerNames.API:
            return APIHandler()
        elif handler_name == HandlerNames.LLAMA:
            return LlamaAPIHandler()
        else:
            raise ValueError(f"Invalid handler name: {handler_name}")
