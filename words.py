"""
This file checks if the word is in the words.txt file.

"""

def words_from_file() -> list[str]:
    """Returns a list of words from the words.txt file."""
    with open("word.txt", "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]
    
if __name__ == "__main__":
    print(words_from_file())