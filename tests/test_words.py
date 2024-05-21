import pytest
@pytest.fixture
def words_from_file() -> list[str]:
    """Returns a list of words from the words.txt file."""
    with open("words.txt", "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]
