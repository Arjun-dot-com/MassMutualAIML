from pydantic import BaseModel, Field, EmailStr

class StudentProfileInput(BaseModel):
    student_email: EmailStr = Field(
        ..., 
        description="Unique identifier for the student"
    )
    student_class: int = Field(
        ..., 
        alias="class", # 'class' is a reserved keyword in Python, so we use an alias
        description="The student's grade level (e.g., 10)"
    )
    subject: str = Field(
        ..., 
        description="The subject the student needs help with (e.g., Mathematics)"
    )
    current_score: float = Field(
        ..., 
        ge=0, le=100, # Ensures the score is strictly between 0 and 100
        description="The student's current score in the subject"
    )
    help_description: str = Field(
        ..., 
        description="Free text written by the student describing their struggles"
    )

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "student_email": "student1@school.com",
                "class": 10,
                "subject": "Mathematics",
                "current_score": 62,
                "help_description": "I struggle with trigonometric identities and probability word problems"
            }
        }