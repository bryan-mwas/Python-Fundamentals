# Module docstring placed at the beginning
# The docstrings follow the Google Python Style Guide
""" Fetches document text from a given URL and prints the words

Usage:
    python3 words.py
"""
import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing words from
        the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Prints items one per line

    Args:
        items: Iterable python types
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a URL.

    Args:
        url: The URL of a UTF-8 text document.
    """
    items = fetch_words(url)
    print_items(items)


# When executed as a script the __name__ attribute evaluates to '__main__'
if __name__ == '__main__' :
    main(sys.argv[1])
