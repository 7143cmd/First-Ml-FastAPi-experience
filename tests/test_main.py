from src.bad_word.main import filter_text
import pytest
@pytest.mark.parametrize(
        "text, filtered_text",
        [
            ("This is a wonderful day but that guy is a fucking asshole!", "This is a wonderful day but that guy is a ####### ########"),
            ("You are asshole bitch!", "You are ####### ######"),
            ("Fuckin moron, stop doing shit, asshole!", "###### ###### stop doing ##### ########"),
        ]
)
def test_filter_text(text, filtered_text):
    assert filter_text(text) == filtered_text