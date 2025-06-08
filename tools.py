import os
from langchain_community.tools import TavilySearchResults
from langchain.agents import tool
from dotenv import load_dotenv
load_dotenv()

tavily_key = os.getenv("TAVILY_API_KEY")
search_tool = TavilySearchResults(api_key=tavily_key)



@tool
def calculator(a: float, b: float, operator: str) -> str:
    """
    A basic calculator that supports +, -, *, and /.
    Parameters:
    - a: First number
    - b: Second number
    - operator: One of '+', '-', '*', '/'
    """
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Error: Unknown operator"


# list of available tools
tools = [search_tool, calculator]
