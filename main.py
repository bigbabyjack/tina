import argparse

from src.datastructures import ServiceContext
from src.llms import LanguageModelNames
from src.orchestrator import LLMOrchestrator


def print_process(service_context: ServiceContext) -> None:
    print(
        f"Input: {service_context.user_input}\n\nOutput: {service_context.parsed_response}"
    )


def main():
    parser = argparse.ArgumentParser(description="Process input query")
    parser.add_argument("query", type=str, nargs="+", help="Input query string")
    args = parser.parse_args()

    query = " ".join(args.query)

    service_context = ServiceContext(
        user_input=query,
        parsed_query=None,
        response="",
        parsed_response=None,
    )
    service_context = LLMOrchestrator(
        service_context,
        model_name=LanguageModelNames.LLAMA3_8B,
    ).orchestrate()
    print_process(service_context)


if __name__ == "__main__":
    main()
