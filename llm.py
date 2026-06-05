def call_llm(context):
    user = context["user"]
    docs = context["documents"]
    
    # Simple logic (instead of real LLM)
    if "employee" in user.lower():
        
        return {
            "tool_call": {
                "name": "get_employee_details",
                "arguments": {"emp_id": "101"}
            }
        }

    
    if docs:
        return {"content": f"Based on docs: {docs}"}

    return {"content": "I don't know."}