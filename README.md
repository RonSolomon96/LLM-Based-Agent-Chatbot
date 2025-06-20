# LLM-Based-Agent Chatbot

This project demonstrates a modular, tool-augmented LLM agent using **LangGraph** and **LangChain**. It supports conversational interactions with tool-calling capabilities such as:

- **Web search** using the Tavily API
- **Mathematical calculations** using a custom calculator tool

---

## Features

- Implements **ReAct-style tool use** via LangGraph
- Dynamically routes between chat and tool
- Includes memory for multiple interactions

---

## Technologies Used

- Python 3.11+
- LangChain
- LangGraph
- OpenAI GPT-4o-mini
- Tavily Search API
---

## How It Works

The system is built using a LangGraph:

1. **User input** is passed as a message.
2. The `chat` node uses the LLM to determine response.
3. If the LLM decides to use a tool:
   - It routes to the `tools` node.
   - Executes the appropriate tool (e.g., search or calculator).
   - Returns to the `chat` node to continue the loop.

---

## Example Prompts

```text
User: What is the capital of Japan?
User: What is 13 * 7?
User: Search for the latest news about SpaceX
---
