# EduSarthi - Your AI Learning Coach
- EduSarthi is a GenAI-powered study assistant designed to make learning interactive rather than passive. Explains concepts,asks questions, evaluate answers and helps improving understanding step by step.
- Explain - Practice - Feedback - Improve
- Students who struggle with concept clarity,
Self learners exploring new domains, 
Learners preparing for exams or interviews

Main Purpose:
The main goal of EduSarthi is to convert learning from a passive activity (reading answers) into an active process (understanding + applying knowledge).

## Problems
Students become dependent on AI-generated answers, 
Conceptual gaps remain unaddressed, 
Learning becomes surface level instead of deep,
check understanding in real time,
In simple terms, AI is helping users complete tasks, but not necessarily learn effectively.
- Passive learning
- Poor concept retention
- Lack of personalized feedback

AI Learning Coach solves this by introducing adaptive learning interactions where the AI actively guides the student through learning and practice.

## Solution
Instead of only answering questions, the system:
- Explains concepts in simple terms
- Gives real-world examples
- Generates quiz questions
- Evaluates student responses
- Adjusts explanation based on performance

Two- way learning process
- AI explains
- User responds
- AI evaluates
- AI adapts

This creates a continuous learning loop that improves understanding.

## Key Features

Learning Features-
- Simplified concept explanations
- Real-world examples to improve clarity
- Structured topic breakdown

Intelligence Features
- Adaptive questioning based on user input
- Context retention using memory
- Personalized responses based on history

Engagement Features
- Interactive quizzes instead of passive reading
- Immediate feedback on answers
- Multi-language support (eg. English, Hindi, Hinglish)

The user is not just consuming information, but actively participating in the learning process.

## How it works

User Input:
- Enters topic and selects preferred language.

Prompt Processing:
- Constructs a structured prompt using LangChain, including previous conversation context.

AI Explanation:
The model generates a simplified explanation along with examples.

Interaction Phase:
- The system asks a quiz question to test understanding.

User Response:
- user submits answer.

Evaluation:
- AI evaluates correctness and provides feedback.

Adaptation:
- If correct then move to a higher level
- If incorrect then re-explain in a simpler way

## Technologies 
- Python - Core programming language
- Streamlit - Interactive web interface
- LangChain - Prompt orchestration and LLM integration
- OpenRouter - LLM API provider
- Openai Model - AI reasoning and generation
- Python-dotenv - Environment variable management

## Project Structure
- `app.py` - Main file
- `prompt.py` - Prompt chaining
- `memory.py` - for conversation memory
- `config.py` - integrate environment varibles with LLM 
- `.env` - API Keys store
- `requirements.txt` - Dependencies
- `readme.md` - This documentation

## Installation
### 1️. Clone the repository
```bash
git clone https://github.com/kaj-al/EDUSARTHI.git
```
### 2️. Create virtual environment
```bash
Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate
```

### 3️. Install dependencies
```bash
pip install -r requirements.txt
```

## Environment Setup
- Create a .env file in the root directory.
`OPENROUTER_API_KEY= your key`
- Run the Application
`streamlit run app.py`

## Example Interaction
User:

    Topic: Machine Learning

    Language: Hinglish

AI Response:

    Machine learning ek technique hai jisme computer data se seekhta hai.

    Quiz:
    Machine learning ka main goal kya hai?

    A) Data se learn karna
    B) Video edit karna
    C) Image crop karna

## Conclusion
EduSarthi represents AI as answering tool to AI as a teaching system.<br>
By combining explanation, interaction, and feedback, it ensures:<br>
Better engagement<br>
Stronger concept clarity<br>
Improved learning outcomes<br>
This project highlights how AI can be used not just for productivity, but for meaningful learning experiences.
