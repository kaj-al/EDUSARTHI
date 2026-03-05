from langchain_core.messages import HumanMessage,AIMessage

class convo:
    def __init__(self):
        self.history = []
    
    def add_user(self,message:str):
        self.history.append(HumanMessage(content=message))
    
    def add_ai(self,message:str):
        self.history.append(AIMessage(content=message))

    def history(self):
        return self.history
    
    def clear(self):
        self.history = []