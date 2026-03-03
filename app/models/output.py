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
    resource_links: str = Field(
        default="Links coming soon", 
        description="The URLs to the video and/or reading material provided in the Available Courses"
    )
class AIAnalysisOutput(BaseModel):
    message: str = Field(..., description="Summary explanation from the AI")
    new_level: str = Field(..., description="Assessed level: beginner | intermediate | advanced")
    updated_recommendation: List[RecommendationItem] = Field(
        ..., 
        description="List of personalized recommendations based on the student's needs"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "message": "Based on your weaknesses, here is your personalized study plan:",
                "new_level": "intermediate",
                "updated_recommendation": [
                    {
                        "chapter": "Trigonometry",
                        "focus_area": "Concept clarity + 20 practice problems on identities",
                        "difficulty": "medium",
                        "priority_score": 0.82
                    }
                ]
            }
        }