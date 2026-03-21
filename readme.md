# EduSarthi - Your AI Learning Coach
- EduSarthi is a GenAI-powered study assistant designed to make learning interactive rather than passive. Explains concepts,asks questions, evaluate answers and helps improving understanding step by step.\
- Explain - Practice - Feedback - Improve

## Problems
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
This creates a continuous learning loop that improves understanding.

## Key Features
- Adaptive Learning Mode
- Quiz Generation
- Performance Feedback
- Conversation Memory
- Multi-Language Support
- Interactive Chat Interface.

## System Architecture

User
   │
   ▼
Streamlit UI
   │
   ▼
LangChain Prompt System
   │
   ▼
LLM (Llama via OpenRouter)
   │
   ▼
AI Learning Coach Logic
   │
   ▼
Response + Quiz + Feedback

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

Example:
Netflix recommendation system.

Quiz:
Machine learning ka main goal kya hai?

A) Data se learn karna
B) Video edit karna
C) Image crop karna

## Future Enhancements
- PDF study material upload
- Knowledge gap detection
- Learning progress dashboard
- Retrieval-Augmented Generation (RAG)
- Personalized learning paths
- Automatic note generation
