import pytest
from app.services.nlp_processor import detect_intent

def test_certification_intent():
    # Keep the test string focused to isolate the certification intent
    text = "Student: Class 9, goal = board exam preparation"
    intent = detect_intent(text)
    assert intent == "certification_preparation"

def test_skill_assessment_intent():
    text = "I am really weak in trigonometric identities and need a quiz."
    intent = detect_intent(text)
    assert intent == "skill_assessment"

def test_topic_exploration_intent():
    text = "I want to explore the basics of Python."
    intent = detect_intent(text)
    assert intent == "topic_exploration"

def test_fallback_intent():
    # If the student just types something vague without our keywords
    text = "I need help with my homework tonight."
    intent = detect_intent(text)
    assert intent == "general_help"