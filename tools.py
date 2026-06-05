#Tools (Function Calling)
def get_employee_details(emp_id):
    fake_db = {
        
        "101": "John Doe - Engineer",
        "102": "Jane Smith - Manager"

    }

    return fake_db.get(emp_id, "Employee not found!")


def get_tools_schema():
    return [
        {
            "name": "get_employee_details",
            "description": "Get employee info using ID",
            "parameters": ["emp_id"]
        }
    ]
