import requests
from src.llms import LLMFactory, LLMAgents
from src.parsers import QueryParser
from src.datastructures import UserInput, QueryResponse, ServiceContext

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
    query = "hello world"
    parser = QueryParser()
    user_input = parser.parse(query)
    print(f"{user_input.query}")
    tina = LLMFactory().get_llm(LLMAgents.LLAMA3_8B)
    query_response = tina.invoke(UserInput(query=query))
    print(query_response.response)


if __name__ == "__main__": 
    main()
