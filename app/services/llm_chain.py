from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from app.models.input import StudentProfileInput
from app.models.output import AIAnalysisOutput
from app.core.config import settings
from langchain_groq import ChatGroq
from app.services.recommender import get_relevant_resources, format_resources_for_prompt 

llm = ChatGroq(
    model="llama-3.3-70b-versatile", 
    temperature=0.0,  # Set to 0.0 for maximum stability and factual adherence
    api_key=settings.GROQ_API_KEY
)

structured_llm = llm.with_structured_output(AIAnalysisOutput)

# Tell the AI to ONLY use the provided courses and strictly extract the links
system_prompt = """
You are an expert AI educational tutor and curriculum planner.
Your goal is to analyze a student's profile and generate a highly personalized study plan.

CRITICAL INSTRUCTION:
You MUST select your recommendations ONLY from the 'Available Courses' provided below. 
Do not invent or hallucinate course titles. Map their specific struggles to the most relevant available course.

IMPORTANT: You MUST extract the 'Video Link' and 'Reading Link' from the Available Courses and populate the 'video_link' and 'reading_link' output fields. If a link is missing, you must output "N/A" for that field.

Assess if their new level is 'beginner', 'intermediate', or 'advanced'.
Keep focus areas concise and actionable.
"""

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "Student Email: {student_email}\n"
              "Class/Grade: {class}\n" 
              "Subject: {subject}\n"
              "Current Score: {current_score}/100\n"
              "Student's Description of Struggles: {help_description}\n\n"
              "--- AVAILABLE COURSES ---\n{available_courses}")
])

analysis_chain = prompt_template | structured_llm

def generate_recommendation(student_data: StudentProfileInput) -> AIAnalysisOutput:
    """
    Retrieves real courses, passes them to the LLM alongside the student data, 
    and returns a guaranteed structured Pydantic output.
    """
    # Fetch and format the real courses based on the student's grade and subject
    raw_courses = get_relevant_resources(student_data.subject, student_data.student_class)
    formatted_courses = format_resources_for_prompt(raw_courses)
    
    # Convert input to dictionary and inject the courses
    input_dict = student_data.model_dump(by_alias=True)
    input_dict["available_courses"] = formatted_courses 
    
    # Run the chain
    result = analysis_chain.invoke(input_dict)
    
    return result