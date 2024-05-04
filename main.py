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
    logging.debug("Creating the service context...")

    context = ServiceContext(
        logger=logging.getLogger(__name__),
        input_query="",
        input_arguments={},
        parsed_query="",
        response="",
        parsed_response="",
        orchestration_plan=[],
    )
    context.logger.debug("Parsing the user input...")
    input_parser = InputArgumentParser()
    context = input_parser.parse(context)
    context.logger.debug(f"Parsed query: {context.parsed_query}")
    context.logger.debug("Starting orchestration planning...")
    context = OrchestratorPlanner().plan(context)
    context.logger.debug(f"Orchestration plan: {context.orchestration_plan}")
    context.logger.debug("Starting orchestration...")
    context = LLMOrchestrator(
        service_context=context,
        model_name=LanguageModelNames.PHI3,
    ).orchestrate()
    context.logger.debug("Orchestration completed")
    context.logger.debug(f"Final service context: {context}")

    print(f"{context.parsed_response}")


if __name__ == "__main__":
    main()
