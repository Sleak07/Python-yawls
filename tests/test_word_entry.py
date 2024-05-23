import random
import pytest

@pytest.fixture
def random_word_entry():
    """Returns a random word entry."""
    return random.randint(0, 100)

def check_word_entry(word_entry):
    assert word_entry >= 0