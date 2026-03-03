from typing import List, Dict

# This acts as a mock database
COURSE_CATALOG = {
    "Mathematics": {
        9: [
            {"title": "Class 9 Maths Foundation (Video Series)", "difficulty": "beginner"},
            {"title": "NCERT Solutions Visual Guide", "difficulty": "beginner"},
            {"title": "Advanced Algebra Olympiad Prep", "difficulty": "hard"}
        ],
        10: [
            {"title": "Board Exam Mastery: Mathematics", "difficulty": "medium"},
            {"title": "Trigonometry & Probability Deep Dive", "difficulty": "hard"},
            {"title": "Class 10 Maths Crash Course", "difficulty": "medium"}
        ]
    },
    "Physics": {
        12: [
            {"title": "JEE Physics Crash Course", "difficulty": "medium"},
            {"title": "JEE Advanced Physics Problem Solving", "difficulty": "hard"},
            {"title": "Class 12 Board Physics Revisions", "difficulty": "easy"}
        ]
    }
}

def get_relevant_resources(subject: str, student_class: int) -> List[Dict[str, str]]:
    """
    Retrieves a list of available courses from the system's catalog 
    based on the student's subject and grade level.
    """
    # Find the subject in our catalog (case-insensitive)
    subject_key = next((key for key in COURSE_CATALOG.keys() if key.lower() == subject.lower()), None)
    
    # If we don't have specific courses for this subject/grade, return a generic fallback
    if not subject_key or student_class not in COURSE_CATALOG[subject_key]:
        return [
            {"title": f"General {subject} Study Guide", "difficulty": "medium"},
            {"title": f"Standard {subject} Practice Modules", "difficulty": "medium"}
        ]
        
    return COURSE_CATALOG[subject_key][student_class]

def format_resources_for_prompt(resources: List[Dict[str, str]]) -> str:
    """
    Converts the list of dictionaries into a clean string format 
    so the LLM can easily read and select from them.
    """
    formatted_list = []
    for res in resources:
        formatted_list.append(f"- {res['title']} (Difficulty: {res['difficulty']})")
    
    return "\n".join(formatted_list)