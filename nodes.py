from langgraph.prebuilt import ToolNode
from langgraph.graph import END , add_messages
from typing import TypedDict, Annotated
from tools import tools
# define intial state 
class AgentState(TypedDict):
    # add_messages concat 2 list (next message)
    messages: Annotated[list, add_messages]
# define graph nodes
tool_node = ToolNode(tools=tools)

def make_chat_node(llm):
    def chat(state):
        output = llm.invoke(state["messages"])
        return {"messages": [output]}
    return chat




def tool_use(state: AgentState):
    last_message = state["messages"][-1]
    tool_calls = getattr(last_message, "tool_calls", [])
    # print tool call
    if tool_calls:
        print("Tool requested:")
        for tool_call in tool_calls:
            print(f"Tool name: {tool_call['name']}")
            print(f"Arguments: {tool_call['args']}")

        return "tools"
    else:
        return END