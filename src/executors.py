from abc import ABC, abstractmethod
import subprocess

from src.datastructures import ServiceContext


class AbstractExecutor(ABC):
    @abstractmethod
    def execute(self, context: ServiceContext) -> ServiceContext:
        pass


class CommandExecutor(AbstractExecutor):
    """
    Documentation for CommandExecutor:
    The CommandExecutor class is an abstract class that defines the interface for executing commands.

    Example:
    class MyCommandExecutor(CommandExecutor):
        def execute(self, context: ServiceContext) -> ServiceContext:
            return context

    my_command_executor = MyCommandExecutor()
    service_context = my_command_executor.execute(service_context)
    """

    def execute(self, context: ServiceContext) -> ServiceContext:
        if context.input_arguments["search"]:
            query = context.input_query
            self.open_google_search(query)
        context.response = f"googling: {context.input_query}"
        return context

    def open_google_search(self, query):
        url = f"https://www.google.com/search?q={query}"
        command = f"open -a 'Google Chrome' '{url}'"
        subprocess.run(command, shell=True)
