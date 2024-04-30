import argparse

from src.datastructures import ServiceContext
from src.llms import LanguageModelNames
from src.orchestrator import LLMOrchestrator


def print_process(service_context: ServiceContext) -> None:
    print(
        f"Input: {service_context.user_input}\n\nOutput: {service_context.parsed_response}"
    )


def process_arguments(args):
    print("Processing arguments:")
    for arg, value in vars(args).items():
        print(f"{arg}: {value}")


def main():
    parser = argparse.ArgumentParser(description="Process input query")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Provides detailed information about the request.",
    )
    parser.add_argument(
        "-c", "--code", action="store_true", help="Indicates a code request"
    )
    parser.add_argument(
        "-s", "--search", action="store_true", help="Indicates a web search request"
    )
    parser.add_argument("query", type=str, nargs="+",
                        help="Input query string")
    args = parser.parse_args()
    process_arguments(args)

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
