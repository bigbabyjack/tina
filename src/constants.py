from enum import StrEnum


class OrchestrationSteps(StrEnum):
    INPUT_ARGUMENT_PARSING = "input_argument_parsing"
    QUERY_PARSING = "query_parsing"
    LLM_INVOCATION = "llm_invocation"
    ACTION_EXECUTION = "action_execution"
    RESPONSE_PARSING = "response_parsing"

    def __repr__(self) -> str:
        return self.value
