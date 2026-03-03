from typing import List, Dict

# This acts as a mock database
COURSE_CATALOG = {
    "Mathematics": {
        9: [
            {"title": "Class 9 Maths Foundation (Video Series)", "difficulty": "beginner", "url": "https://youtube.com/playlist?list=math9_foundation"},
            {"title": "NCERT Solutions Visual Guide", "difficulty": "beginner", "url": "https://example.com/pdfs/ncert_math9.pdf"},
            {"title": "Advanced Algebra Olympiad Prep", "difficulty": "hard", "url": "https://youtube.com/watch?v=algebra_prep"}
        ],
        10: [
            {"title": "Board Exam Mastery: Mathematics", "difficulty": "medium", "url": "https://youtube.com/playlist?list=math10_board"},
            {"title": "Trigonometry & Probability Deep Dive", "difficulty": "hard", "url": "https://example.com/pdfs/trig_prob_10.pdf"},
            {"title": "Class 10 Maths Crash Course", "difficulty": "medium", "url": "https://youtube.com/watch?v=math10_crash"}
        ]
    },
    "Physics": {
        12: [
            {"title": "JEE Physics Crash Course", "difficulty": "medium", "url": "https://youtube.com/playlist?list=jee_physics"},
            {"title": "JEE Advanced Physics Problem Solving", "difficulty": "hard", "url": "https://example.com/pdfs/jee_adv_physics.pdf"},
            {"title": "Class 12 Board Physics Revisions", "difficulty": "easy", "url": "https://youtube.com/watch?v=physics12_revision"}
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
            {"title": f"General {subject} Study Guide", "difficulty": "medium", "url": f"https://example.com/search?q={subject}+guide"},
            {"title": f"Standard {subject} Practice Modules", "difficulty": "medium", "url": f"https://example.com/search?q={subject}+practice"}
        ]
        
    return COURSE_CATALOG[subject_key][student_class]

def format_resources_for_prompt(resources: List[Dict[str, str]]) -> str:
    """
    Converts the list of dictionaries into a clean string format 
    so the LLM can easily read and select from them.
    """
    formatted_list = []
    for res in resources:
        # We now include the URL in the prompt so the LLM can see it and return it
        formatted_list.append(f"- {res['title']} (Difficulty: {res['difficulty']}) [Link: {res['url']}]")
    
    return "\n".join(formatted_list)