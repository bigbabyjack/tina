# tina
A local Terminal Agent leveraging the large language model Llama3.

## Design
Image of current design plan:

![tina](./static/design_01.png)

## Supported Models
- LlaMa3:8B
- gemma:2B
- Mixtral:8x7B

## Dev Roadmap
- [x] add user input from stdin
- [x] define an action for tina to carry out: display code in a single line
- [x] define an action for tina to carry out: search google
- [x] implement planner and clean up orchestration using claude suggestions
- [x] add logging
- [ ] introduce a second, faster model for quicker iteration
- [ ] add system for prompts
- [ ] multiturn?
- [ ] add streaming capability
- [ ] ...
