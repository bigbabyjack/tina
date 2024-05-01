from abc import ABC, abstractmethod

from dataclasses import dataclass
from enum import StrEnum


class LanguageModelFamily(StrEnum):
    """
    Supported language model families
    """

    LLAMA = "llama"


class LanguageModelNames(StrEnum):
    """
    The LanguageModelNames enum is an enum class that defines the names of the supported language models.
    """

    LLAMA3_8B = "llama3:8b"


class AbstractLanguageModelConfig(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        pass


@dataclass
class LanguageModelConfig:
    """
    The LanguageModelConfig class is a dataclass that defines the configuration for a language model.
    The model_name, url, headers, and options attributes are required.
    The to_dict() method is used to convert the object to a dictionary.

    Example:
    config = LanguageModelConfig(
        model_name=LanguageModelNames.LLAMA3_8B,
        url="http://127.0.0.1:11434/api/generate",
        headers={"Content-Type": "application/json"},
        options={"model": LanguageModelNames.LLAMA3_8B, "stream": False},
    )
    """

    model_family: LanguageModelFamily
    model_name: LanguageModelNames
    api_url: str
    headers: dict
    options: dict

    def to_dict(self) -> dict:
        return {
            "headers": self.headers,
            "model_family": self.model_family,
            "model_name": self.model_name,
            "api_url": self.api_url,
            "options": self.options,
        }


class AbstractLanguageModelConfigRetriever(ABC):
    @abstractmethod
    def get_config(self) -> LanguageModelConfig:
        pass


class LanguageModelConfigRetriever:
    """
    The LanguageModelConfigRetriever class is a class that provides a method to get a LanguageModelConfig object based on the model name.

    Example:
    config = LanguageModelConfigRetriever(model_name=LanguageModelNames.LLAMA3_8B).get_config()
    print(config.to_dict())

    The get_config() method should be implemented by subclasses to return a LanguageModelConfig object based on the model name.
    """

    def __init__(self, model_name: LanguageModelNames):
        self.model_name = model_name

    def get_config(self) -> LanguageModelConfig:
        if self.model_name == LanguageModelNames.LLAMA3_8B:
            return LanguageModelConfig(
                model_family=LanguageModelFamily.LLAMA,
                model_name=self.model_name,
                api_url="http://127.0.0.1:11434/api/generate",
                headers={"Content-Type": "application/json"},
                options={
                    "model": self.model_name,
                    "stream": False,
                },
            )
        raise ValueError(f"Invalid model name: {self.model_name}")
