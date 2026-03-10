
from config import llm
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an AI Learning Coach.
Process:
1. Explain the concept simply but thoroughly.
2. Give a small real-world example.
3. Ask ONE multiple choice quiz question according to the explanation you provided.
4. Wait for student answer.
5. If correct then appreciate and give slightly harder question.
6. If wrong then explain again simply.

Always respond in the selected language.
"""
    ),
    MessagesPlaceholder("chat_history"),
    ("human", "Topic or answer: {input}\nLanguage: {language}")
])

chain = prompt | llm


def get_response(user_input, language, memory):
    response = chain.invoke({
        "input": user_input,
        "language": language,
        "chat_history": memory.get_history()
    })

    memory.add_user(user_input)
    memory.add_ai(response.content)

    return response.content

