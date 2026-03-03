from typing import List, Dict

# This acts as our real curriculum database
COURSE_CATALOG = {
    "Mathematics": {
        10: [
            {
                "title": "Real Numbers", "domain": "Arithmetic", "difficulty": "easy",
                "youtube_url": "https://www.youtube.com/watch?v=-UdHmSTmQtw",
                "website_url": "https://byjus.com/ncert-solutions-class-10-maths/chapter-1-real-numbers/"
            },
            {
                "title": "Polynomials", "domain": "Algebra", "difficulty": "medium",
                "youtube_url": "https://www.youtube.com/watch?v=kiegUjhq8Ao",
                "website_url": "https://byjus.com/ncert-solutions-class-10-maths/chapter-2-polynomials/"
            },
            {
                "title": "Pair of Linear Equations in Two Variables", "domain": "Algebra", "difficulty": "medium",
                "youtube_url": "https://www.youtube.com/watch?v=uz1yjvlu-RU",
                "website_url": "https://byjus.com/ncert-solutions-class-10-maths/chapter-3-linear-equations-in-two-variables/"
            },
            {
                "title": "Quadratic Equations", "domain": "Algebra", "difficulty": "hard",
                "youtube_url": "https://www.youtube.com/watch?v=hayFtYnAB-Q",
                "website_url": "https://byjus.com/ncert-solutions-class-10-maths/chapter-4-quadratic-equations/"
            },
            {
                "title": "Arithmetic Progressions", "domain": "Arithmetic", "difficulty": "medium",
                "youtube_url": "https://youtu.be/vsGPaLIAW10?si=loAjJy5sJBfCRnJ9",
                "website_url": "https://byjus.com/ncert-solutions-class-10-maths/chapter-5-arithmetic-progressions/"
            },
            {
                "title": "Triangles", "domain": "Geometry", "difficulty": "hard",
                "youtube_url": "https://youtu.be/nxo1ItY3oTo?si=J7zY_1ANi0an_Nak",
                "website_url": "https://byjus.com/ncert-solutions-class-10-maths/chapter-6-triangles/"
            },
            {
                "title": "Coordinate Geometry", "domain": "Geometry", "difficulty": "medium",
                "youtube_url": "https://youtu.be/TXDyGK_GdNM?si=FkITYZyVLi9LfChW",
                "website_url": "https://byjus.com/ncert-solutions-class-10-maths/chapter-7-coordinate-geometry/"
            },
            {
                "title": "Introduction to Trigonometry", "domain": "Trigonometry", "difficulty": "hard",
                "youtube_url": "https://youtu.be/wdaBwIv7Jso?si=z-njhrsHQvc3m8_1",
                "website_url": "https://byjus.com/ncert-solutions-class-10-maths/chapter-8-introduction-to-trigonometry/"
            },
            {
                "title": "Some Applications of Trigonometry", "domain": "Trigonometry", "difficulty": "hard",
                "youtube_url": "https://youtu.be/otABxL0TP6U?si=3n_mTOlVeXTPq6Lb",
                "website_url": "https://byjus.com/ncert-solutions-class-10-maths/chapter-9-some-applications-of-trigonometry/"
            },
            {
                "title": "Circles", "domain": "Geometry", "difficulty": "medium",
                "youtube_url": "https://youtu.be/dazX40Ct7J0?si=TUuWCJaaKMT3IkWG",
                "website_url": "https://byjus.com/ncert-solutions-class-10-maths/chapter-10-circles/"
            },
            {
                "title": "Areas Related to Circles", "domain": "Geometry", "difficulty": "medium",
                "youtube_url": "https://youtu.be/usf6lf_3DnU?si=v0SnvKtEMNryB4rN",
                "website_url": "https://byjus.com/ncert-solutions-class-10-maths/chapter-12-areas-related-to-circles/"
            },
            {
                "title": "Surface Areas and Volumes", "domain": "Geometry", "difficulty": "hard",
                "youtube_url": "https://www.youtube.com/live/P4bnYvV15Rk?si=CDV1vaTRctFJ0y-B",
                "website_url": "https://byjus.com/ncert-solutions-class-10-maths/chapter-13-surface-areas-and-volumes/"
            },
            {
                "title": "Statistics", "domain": "Statistics", "difficulty": "medium",
                "youtube_url": "https://www.youtube.com/live/WOKchTFXnYo?si=w5J-oXBfM8Al_qOK",
                "website_url": "https://byjus.com/ncert-solutions-class-10-maths/chapter-14-statistics/"
            },
            {
                "title": "Probability", "domain": "Statistics", "difficulty": "easy",
                "youtube_url": "https://www.youtube.com/live/NXH-pH_H_yg?si=vRdxbldkyvIU2w_u",
                "website_url": "https://byjus.com/ncert-solutions-class-10-maths/chapter-15-probability/"
            }
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
    
    # If we don't have specific courses for this subject/grade, return an empty list or generic fallback
    if not subject_key or student_class not in COURSE_CATALOG[subject_key]:
        return []
        
    return COURSE_CATALOG[subject_key][student_class]

def format_resources_for_prompt(resources: List[Dict[str, str]]) -> str:
    """
    Converts the list of dictionaries into a clean string format 
    so the LLM can easily read and select from them.
    """
    if not resources:
        return "No specific courses available for this grade and subject."

    formatted_list = []
    for res in resources:
        # Combine all the new data into a highly structured prompt string
        formatted_list.append(
            f"- Topic: {res['title']} | Domain: {res['domain']} | Difficulty: {res['difficulty']}\n"
            f"  Video Link: {res['youtube_url']}\n"
            f"  Reading Link: {res['website_url']}"
        )
    
    return "\n\n".join(formatted_list)