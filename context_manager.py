#context_manager.py
class ContextManager:
    def __init__(self, memory, retriever, tools):
        self.memory = memory
        self.retriever = retriever
        self.tools = tools

    def build_content(self, user_query):
        return {
            "system":"You are a helpful assistant",
            "user": user_query,
            "history": self.memory.get_recent(),
            "documents": self.retriever.search(user_query),
            "tools": self.tools
        }