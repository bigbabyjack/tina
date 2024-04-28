from dataclasses import dataclass
from enum import StrEnum

# Set the URL for the LLaMA model's chat API endpoint
url = "http://127.0.0.1:11434/api/generate"

# Set the headers for the request

# Set the data for the chat API request
data = {
    "model": "llama3:8b",
    "prompt": "I am making a CLI tool that uses Llama3 as an agent for carrying out different actions based on the user text input.",
    "stream": False,
}


class LLMAgents(StrEnum):
    LLAMA3_8B = "llama3:8b"


@dataclass
class LLMConfig:
    model_name: LLMAgents
    url: str
    headers: dict
    options: dict

    def to_dict(self):
        return {
            "model_name": self.model_name,
            "url": self.url,
            "headers": self.headers,
            "options": self.options,
        }


class LLMConfigRetriever:
    def __init__(self, model_name: LLMAgents):
        self.model_name = model_name

    def get_config(self) -> LLMConfig:
        if self.model_name == LLMAgents.LLAMA3_8B:
            return LLMConfig(
                model_name=self.model_name,
                url="http://127.0.0.1:11434/api/generate",
                headers={"Content-Type": "application/json"},
                options={
                    "model": self.model_name,
                    "stream": False,
                },
            )
        raise ValueError(f"Invalid model name: {self.model_name}")
