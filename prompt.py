from langchain_core.prompts import ChatPromptTemplate
from config import llm



prompt = ChatPromptTemplate.from_messages([
   ("system","You are a helpful AI teacher. Explain clearly in simple English and then language specified by user"),
   ("placeholder","{history}"),
   ("human","{input}\nLangauge:{language}")
])

chain = prompt | llm

def response(input,language,memory):
    response = chain.invoke({
        "input":input,
        "language":language,
        "history":memory.history(),
    })

    memory.add_user(input)
    memory.add_ai(response.content)
    
    return response.content

