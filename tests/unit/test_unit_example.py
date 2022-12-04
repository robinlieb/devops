from app import generate_greeting

def test_generate_greeting():
    result = generate_greeting("John")

    assert result == "Hello John"