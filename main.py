from memory import Memory
from retriever import Retriever
from tools import get_employee_details, get_tools_schema
from context_manager import ContextManager
from llm import call_llm

memory = Memory()
retriever = Retriever()
tools = get_tools_schema()

context_manager = ContextManager(memory, retriever, tools)

def handle_query(user_query):
    context = context_manager.build_content(user_query)
    response = call_llm(context)

    #tool execution

    if "tool_call" in response:
        tool = response["tool_call"]
        result = get_employee_details(tool["arguments"]["emp_id"])

        final_answer = f"Tool result :{result}"

    else:
        final_answer = response["content"]

    memory.add(user_query, final_answer)
    return final_answer

#Run
while True:
    query = input("You: ")
    print("AI:", handle_query(query))
