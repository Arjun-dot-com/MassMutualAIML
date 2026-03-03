# AI-Powered Personalized Learning Platform

This repository contains the source code for an AI-driven web-based platform that analyzes student profiles, assesses learning needs, and provides customized recommendations for courses and resources. 

This project is designed to simulate a scalable enterprise tool for personalized education without relying on real-time conversational interactions.

---

## Team Contributions

* **Vijayakumar Arjun**: Architected and developed the `ai-service` microservice. Implemented the FastAPI backend, Pydantic data validation contracts, spaCy-based Natural Language Processing for intent detection, and the LangChain/OpenAI Retrieval-Augmented Generation (RAG) pipeline for structured course recommendations.
* **Anumita Choubey**: Developed the `frontend` user interface and the `core-backend` infrastructure. Handled database management, user authentication, and the API integration connecting the user-facing web app to the AI microservice.

---

## Monorepo Architecture

This repository is structured as a monorepo containing three distinct services:

1. **ai-service/**: A Python/FastAPI microservice handling all NLP, LLM, and recommendation logic.
2. **core-backend/**: The primary backend handling database operations and business logic.
3. **frontend/**: The web-based user interface for student input and dashboard visualization.
4. **docs/**: Contains the final Project Report, architecture diagrams, and the demonstration video.

---

## AI Service Features

* **Strict Data Contracts**: Utilizes Pydantic to ensure all incoming and outgoing data strictly adheres to the predefined JSON schemas (`ai_input_contract` and `ai_output_contract`).
* **Intent Detection**: Uses a lightweight, rule-based NLP model (spaCy) to quickly categorize student goals (e.g., skill assessment, topic exploration, certification preparation) before routing to the LLM.
* **RAG Recommendation Engine**: Maps the student's needs against an internal course catalog and dynamically injects valid, available courses into the LLM prompt to prevent AI hallucinations.
* **Structured Output**: Forces the LLM to return strictly formatted JSON data for seamless frontend integration.

---

## Local Setup Instructions (AI Service)

Follow these steps to run the AI microservice locally.

### 1. Environment Setup

Navigate to the AI service directory and install the required Python dependencies:

`cd ai-service`
`pip install -r requirements.txt`
`python -m spacy download en_core_web_sm`

### 2. Configuration

Create a `.env` file in the root of the `ai-service` directory and add your OpenAI API key:

`OPENAI_API_KEY="sk-your-api-key-here"`

### 3. Running the Server

Start the FastAPI application using Uvicorn:

`uvicorn app.main:app --reload`

The service will be available at `http://127.0.0.1:8000`. You can access the interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.

### 4. Running Tests

To verify the NLP intent detection and LLM data contract mocks, run the pytest suite:

`pytest -v`

---

## API Endpoints

### `POST /analyze`

Analyzes a student's profile and returns a personalized study plan.

**Expected Input Payload:**
Requires `student_email`, `class`, `subject`, `current_score`, and `help_description`.

**Expected Output Response:**
Returns a structured JSON object containing a summary `message`, the student's `new_level`, and an `updated_recommendation` array featuring specific chapters, focus areas, difficulty levels, and priority scores.