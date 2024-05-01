import logging

from src.logger import setup_logging, timemethod
from src.datastructures import ServiceContext
from src.llms import LanguageModelNames
from src.orchestrator import LLMOrchestrator
from src.planners import OrchestratorPlanner
from src.parsers import InputArgumentParser


@timemethod
def main():
    setup_logging()
    logging.debug("Starting the program...")

    context = ServiceContext(
        logger=logging.getLogger(__name__),
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
