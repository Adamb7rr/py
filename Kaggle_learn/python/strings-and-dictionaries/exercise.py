# strings_exercises.py


# --- 1. Zip Code Validator ---
def is_valid_zip(zip_code):
    """Return True if zip_code is exactly 5 digits."""
    return len(zip_code) == 5 and zip_code.isdigit()


# --- 2. Word Search ---
def word_search(doc_list, keyword):
    """
    Takes a list of documents (strings) and a keyword.
    Returns a list of indices of documents containing the keyword.
    Matching is case-insensitive.
    Periods and commas are ignored.
    """
    indices = []

    for i, doc in enumerate(doc_list):
        tokens = doc.split()
        normalized = [token.rstrip('.,').lower() for token in tokens]

        if keyword.lower() in normalized:
            indices.append(i)

    return indices


# --- 3. Multi-Word Search ---
def multi_word_search(doc_list, keywords):
    """
    Returns a dictionary mapping each keyword to a list of document indices
    containing that keyword.
    """
    keyword_to_indices = {}

    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(doc_list, keyword)

    return keyword_to_indices


# --- Test Block ---
if __name__ == "__main__":

    # Zip test
    print("Zip test 12345:", is_valid_zip("12345"))  # True
    print("Zip test 1234a:", is_valid_zip("1234a"))  # False

    # Word search test
    docs = [
        "The Learn Python Challenge Casino.",
        "They bought a car and a casino",
        "Casinoville"
    ]

    print("Word search (casino):", word_search(docs, "casino"))
    print("Multi word search:", multi_word_search(docs, ["casino", "they"]))