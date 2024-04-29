from dataclasses import dataclass
from enum import StrEnum


class LanguageModelNames(StrEnum):
    LLAMA3_8B = "llama3:8b"


@dataclass
class LanguageModelConfig:
    model_name: LanguageModelNames
    url: str
    headers: dict
    options: dict

    def to_dict(self) -> dict:
        return {
            "model_name": self.model_name,
            "url": self.url,
            "headers": self.headers,
            "options": self.options,
        }


class LanguageModelConfigRetriever:
    def __init__(self, model_name: LanguageModelNames):
        self.model_name = model_name

    def get_config(self) -> LanguageModelConfig:
        if self.model_name == LanguageModelNames.LLAMA3_8B:
            return LanguageModelConfig(
                model_name=self.model_name,
                url="http://127.0.0.1:11434/api/generate",
                headers={"Content-Type": "application/json"},
                options={
                    "model": self.model_name,
                    "stream": False,
                },
            )
        raise ValueError(f"Invalid model name: {self.model_name}")
