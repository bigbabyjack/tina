from abc import ABC, abstractmethod

from src.planners import OrchestrationSteps
from src.datastructures import ServiceContext
from src.llms import LLMFactory, LanguageModelNames
from src.parsers import QueryParser, ResponseParser
from src.executors import CommandExecutor


class AbstractOrchestrator(ABC):
    @abstractmethod
    def orchestrate(self) -> ServiceContext:
        pass


class LLMOrchestrator(AbstractOrchestrator):
    def __init__(self, service_context: ServiceContext, model_name: LanguageModelNames):
        self.model_name = model_name
        self.service_context = service_context

    def orchestrate(self) -> ServiceContext:
        for step in self.service_context.orchestration_plan.plan:
            if step == OrchestrationSteps.QUERY_PARSING:
                self.query_parser = QueryParser()
                self.service_context = self.query_parser.parse(self.service_context)
            elif step == OrchestrationSteps.LLM_INVOCATION:
                self.llm = LLMFactory().get_llm(self.model_name)
                self.service_context = self.llm.invoke(self.service_context)
            elif step == OrchestrationSteps.ACTION_EXECUTION:
                self.command_executor = CommandExecutor().execute(self.service_context)
            elif step == OrchestrationSteps.RESPONSE_PARSING:
                self.response_parser = ResponseParser()
                self.service_context = self.response_parser.parse(self.service_context)
        return self.service_context
