from fastapi import APIRouter, HTTPException
from app.models.input import StudentProfileInput
from app.models.output import AIAnalysisOutput
from app.services.llm_chain import generate_recommendation
from app.services.nlp_processor import detect_intent  # Import the NLP module

router = APIRouter(
    prefix="/analyze",
    tags=["Analysis"]
)

@router.post("/", response_model=AIAnalysisOutput)
async def analyze_student_profile(payload: StudentProfileInput):
    try:
        # 1. Run the fast NLP intent detection
        student_intent = detect_intent(payload.help_description)
        
        # 2. You can dynamically modify the prompt based on intent!
        # For example, appending the detected intent to the student's description
        # so the LLM knows exactly what mode to be in.
        enhanced_description = f"[Detected Goal: {student_intent.replace('_', ' ').title()}] {payload.help_description}"
        payload.help_description = enhanced_description
        
        # 3. Pass the enhanced data to the heavy-lifting LLM
        ai_response = generate_recommendation(payload)
        
        return ai_response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Processing Error: {str(e)}")