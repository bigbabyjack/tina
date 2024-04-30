from src.datastructures import ServiceContext
from src.llms import LanguageModelNames
from src.orchestrator import LLMOrchestrator


def main():
    context = LLMOrchestrator(
        ServiceContext(
            input_query="",
            input_arguments={},
            parsed_query="",
            response="",
            parsed_response="",
        ),
        model_name=LanguageModelNames.LLAMA3_8B,
    ).orchestrate()

    print(f"{context.parsed_response}")


if __name__ == "__main__":
    main()
