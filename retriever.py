#retriever (RAG)

documents = [
    "Company leave policy is 20 days per year",
    "Office timings are 9 AM to 6 PM",
    "Employees can work remotely twice a week"
]

class Retriever:
    def search(self, query):
        results = []
        for doc in documents:
            if any(word.lower() in doc.lower() for word in query.split()):
                results.append(doc)
        
        return results[:2]