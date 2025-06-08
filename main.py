# from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
import nodes 
from langgraph.graph import END , StateGraph, add_messages
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from tools import tools
load_dotenv()

############## Setup Gemini #############
memory = MemorySaver()


# ############# Setup Gemini #############
# api_key = os.getenv("GOOGLE_API_KEY")
# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash-latest",
#     google_api_key=api_key
# )

# ############# Setup gpt #############
llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

# bind the llm with tools(e.g. tavily)
llm_with_tools = llm.bind_tools(tools=tools)



# build graph   
graph = StateGraph(nodes.AgentState)
graph.add_node("chat", nodes.make_chat_node(llm_with_tools))
graph.set_entry_point("chat")
graph.add_node("tools", nodes.tool_node)
graph.add_conditional_edges("chat",nodes.tool_use)
graph.add_edge("tools", "chat")

# start 
# for exit type exit 
app = graph.compile(checkpointer=memory)
config = { "configurable": {
          "thread_id":1
        }
         }

while True:
    user_input = input("User:")
    if user_input == "exit":
        break
    else:
        r = app.invoke({"messages": [HumanMessage(content=user_input)]},config=config)
        print(r["messages"][-1].content)

