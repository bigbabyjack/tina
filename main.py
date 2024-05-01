from src.datastructures import ServiceContext
from src.llms import LanguageModelNames
from src.orchestrator import LLMOrchestrator
from src.planners import OrchestratorPlanner
from src.parsers import InputArgumentParser


def main():
    context = ServiceContext(
        input_query="",
        input_arguments={},
        parsed_query="",
        response="",
        parsed_response="",
        orchestration_plan=[],
    )
    input_parser = InputArgumentParser()
    context = input_parser.parse(context)
    context = OrchestratorPlanner().plan(context)
    context = LLMOrchestrator(
        service_context=context,
        model_name=LanguageModelNames.LLAMA3_8B,
    ).orchestrate()

    print(f"{context.parsed_response}")


if __name__ == "__main__":
    main()
