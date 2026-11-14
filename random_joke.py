"""Fetch and display a random joke from the Official Joke API."""

import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API_URL = "https://official-joke-api.appspot.com/random_joke"


def get_random_joke() -> tuple[str, str]:
    """Return a joke's setup and punchline from the external API."""
    request = Request(API_URL, headers={"User-Agent": "DSA-random-joke-generator/1.0"})

    try:
        with urlopen(request, timeout=10) as response:
            joke = json.load(response)
    except (HTTPError, URLError, TimeoutError) as error:
        raise RuntimeError(f"Could not fetch a joke: {error}") from error
        
    try:
        return joke["setup"], joke["punchline"]
    except (TypeError, KeyError) as error:
        raise RuntimeError("The joke API returned an unexpected response.") from error


def main() -> None:
    try:
        setup, punchline = get_random_joke()
    except RuntimeError as error:
        print(error)
        return

    print(setup)
    input("Press Enter for the punchline...")
    print(punchline)


if __name__ == "__main__":
    main()
