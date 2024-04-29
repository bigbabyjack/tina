import requests

from src.llms import LanguageModelNames
from src.orchestrator import LLMOrchestrator

# # Set the URL for the LLaMA model's chat API endpoint
# url = "http://127.0.0.1:11434/api/generate"
#
# # Set the headers for the request
#
# # Set the data for the chat API request
# data = {
#     "model": "llama3:8b",
#     "prompt": "I am making a CLI tool that uses Llama3 as an agent for carrying out different actions based on the user text input.",
#     "stream": False,
# }
#
# # Send a POST request to the LLaMA model's chat API endpoint
# response = requests.post(url, json=data)
# response.raise_for_status()
# response = response.json()
#
# message_response = response["response"]
# print(message_response)


def main():
    query = "I am building a tool!"
    orchestrator = LLMOrchestrator(model_name=LanguageModelNames.LLAMA3_8B)
    query_response = orchestrator.orchestrate(query)
    print(query_response.response)


if __name__ == "__main__":
    main()
