from model import filter_text
import pytest
from main import app
from fastapi.testclient import TestClient

@pytest.mark.parametrize(
        "text, filtered_text",
        [
            ("This is a wonderful day but that guy is a fucking asshole!", "This is a wonderful day but that guy is a ####### ########"),
            ("Do you like play football? I vote for the team named <<Shahtar>>", "Do you like play football? I vote for the team named <<Shahtar>>"),
            ("You are asshole bitch!", "You are ####### ######"),
            ("Fuckin moron, stop doing shit, asshole!", "###### ###### stop doing ##### ########"),
            ("The sun is shining brightly today.", "The sun is shining brightly today."),
            ("She loves reading books in her free time.", "She loves reading books in her free time."),
            ("They went to the park to play football.", "They went to the park to play football."),
            ("Coffee tastes better in the morning.", "Coffee tastes better in the morning."),
            ("He is learning to play the guitar.", "He is learning to play the guitar."),
            ("The movie we watched last night was amazing.", "The movie we watched last night was amazing."),
            ("I need to buy some groceries after work.", "I need to buy some groceries after work."),
            ("Her dog is very friendly and playful.", "Her dog is very friendly and playful."),
            ("We are planning a trip to the mountains.", "We are planning a trip to the mountains."),
            ("The teacher explained the lesson clearly.", "The teacher explained the lesson clearly."),
            ("You're such an idiot for doing that.", "You're such an ##### for doing that."),
            ("This damn computer keeps crashing!", "This #### computer keeps crashing!"),
            ("Shut the hell up and listen!", "Shut the #### up and listen!"),
            ("What the fuck is wrong with you?", "What the #### is wrong with you?"),
            ("Don’t be such a lazy ass.", "Don’t be such a lazy ass."),
            ("This traffic is bullshit!", "This traffic is #########"),
            ("Go to hell with your stupid ideas.", "Go to #### with your stupid ideas."),
            ("I don’t give a shit about your excuses.", "I don’t give a #### about your excuses."),
            ("You’re a complete moron sometimes.", "You’re a complete ##### sometimes."),
            ("Why are you so goddamn annoying?", "Why are you so ####### annoying?")
        ]
)
def test_filter_text(text, filtered_text):
    assert filter_text(text) == filtered_text


def test_client():
    client = TestClient(app)
    text = "Go to hell with your stupid ideas."
    response = client.post("/censored", json={"text": text})

    assert response.status_code == 200

    data = response.json()
    assert data["result"] == "Go to #### with your stupid ideas."
