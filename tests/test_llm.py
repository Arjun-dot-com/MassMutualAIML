import pytest
from unittest.mock import patch
from app.models.input import StudentProfileInput
from app.models.output import AIAnalysisOutput, RecommendationItem
from app.services.llm_chain import generate_recommendation

@pytest.fixture
def mock_student_input():
    return StudentProfileInput(
        student_email="test@student.com",
        student_class=10,
        subject="Mathematics",
        current_score=62.0,
        help_description="I struggle with probability word problems"
    )

@pytest.fixture
def mock_llm_output():
    return AIAnalysisOutput(
        message="Here is your custom plan.",
        new_level="intermediate",
        updated_recommendation=[
            RecommendationItem(
                chapter="Probability",
                focus_area="Application-based word problems",
                difficulty="hard",
                priority_score=0.85
            )
        ]
    )

# Patch the whole chain object instead of the method
@patch("app.services.llm_chain.analysis_chain")
def test_generate_recommendation_structure(mock_analysis_chain, mock_student_input, mock_llm_output):
    # Set the return value for the invoke method on our mock
    mock_analysis_chain.invoke.return_value = mock_llm_output
    
    # Run the function
    result = generate_recommendation(mock_student_input)
    
    # Verify the output format
    assert result.new_level == "intermediate"
    assert len(result.updated_recommendation) == 1
    assert result.updated_recommendation[0].chapter == "Probability"
    assert result.updated_recommendation[0].difficulty == "hard"
    
    # Verify that the chain was actually called
    mock_analysis_chain.invoke.assert_called_once()