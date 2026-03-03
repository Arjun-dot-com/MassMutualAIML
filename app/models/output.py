from pydantic import BaseModel, Field
from typing import List

class RecommendationItem(BaseModel):
    chapter: str = Field(..., description="Detected chapter or topic")
    focus_area: str = Field(..., description="Specific area the student should focus on")
    difficulty: str = Field(..., description="Recommended difficulty level (e.g., easy, medium, hard)")
    priority_score: float = Field(
        ..., 
        ge=0.0, le=1.0, 
        description="Relevance score between 0.0 and 1.0"
    )
    # Reverted to strict strings to prevent Groq API validation errors
    video_link: str = Field(..., description="The exact YouTube URL provided in the Available Courses. If none, output 'N/A'")
    reading_link: str = Field(..., description="The exact website URL provided in the Available Courses. If none, output 'N/A'")

class AIAnalysisOutput(BaseModel):
    message: str = Field(..., description="Summary explanation from the AI")
    new_level: str = Field(..., description="Assessed level: beginner | intermediate | advanced")
    updated_recommendation: List[RecommendationItem] = Field(
        ..., 
        description="List of personalized recommendations based on the student's needs"
    )