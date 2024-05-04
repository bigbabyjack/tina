# tina
A local Terminal Agent leveraging the large language model Llama3.

## Requirements
- [Ollama](https://ollama.com/)
- One of the [supported models](#supported-ollama-models)
- [Python3](https://www.python.org/downloads/)

## Supported Ollama Models
- LlaMa3:8B
- Phi3:Latest
- Mixtral:8x7B

## Dev Roadmap
- [x] add user input from stdin
- [x] define an action for tina to carry out: display code in a single line
- [x] define an action for tina to carry out: search google
- [x] implement planner and clean up orchestration using claude suggestions
- [x] add logging
- [x] introduce a second, faster model for quicker iteration
- [ ] add system for prompts
- [ ] multiturn?
- [ ] add streaming capability
- [ ] ...
