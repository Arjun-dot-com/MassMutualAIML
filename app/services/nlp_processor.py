import spacy
from spacy.matcher import Matcher

# Load the lightweight English NLP model
# Note: You will need to run `python -m spacy download en_core_web_sm` in your terminal first
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading spaCy model...")
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Initialize the rule-based matcher
matcher = Matcher(nlp.vocab)

# Define vocabulary patterns for the required intents
# 1. Skill Assessment 
assessment_patterns = [
    [{"LOWER": {"IN": ["test", "quiz", "assess", "evaluate", "score"]}}],
    [{"LOWER": "don't"}, {"LOWER": "know"}, {"LOWER": "my"}, {"LOWER": "level"}],
    [{"LOWER": "weak"}, {"LOWER": "in"}]
]

# 2. Topic Exploration
exploration_patterns = [
    [{"LOWER": {"IN": ["explore", "learn", "start", "basics", "introduction"]}}],
    [{"LOWER": "new"}, {"LOWER": "to"}],
    [{"LOWER": "want"}, {"LOWER": "to"}, {"LOWER": "know"}, {"LOWER": "about"}]
]

# 3. Certification / Exam Preparation
certification_patterns = [
    [{"LOWER": {"IN": ["cert", "certification", "exam", "board", "jee", "pass"]}}],
    [{"LOWER": "prepare"}, {"LOWER": "for"}]
]

# Add patterns to the matcher
matcher.add("SKILL_ASSESSMENT", assessment_patterns)
matcher.add("TOPIC_EXPLORATION", exploration_patterns)
matcher.add("CERTIFICATION_PREPARATION", certification_patterns)

def detect_intent(text: str) -> str:
    """
    Analyzes the student's help description to determine their primary learning goal.
    Returns one of the core intents or a fallback 'general_help'.
    """
    doc = nlp(text)
    matches = matcher(doc)
    
    # If no specific patterns are matched, default to general help
    if not matches:
        return "general_help"
        
    # Find the most frequent or first matched intent
    # Matches return a tuple: (match_id, start, end)
    match_id = matches[0][0] 
    intent_string = nlp.vocab.strings[match_id]
    
    return intent_string.lower()