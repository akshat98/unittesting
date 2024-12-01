VOWELS = ("a", "e", "i", "o", "u")


def find_vowels(name: str) -> int:
    """Count the number of vowels in a name."""
    return sum(1 for ch in name.lower() if ch in VOWELS)


def name_mapping(names):
    """
    Maps names into vowel and consonant categories.
    Calculates vowels and consonants for each name.
    """
    # Create a dictionary mapping names to their vowel counts
    vowel = {name: find_vowels(name) for name in names}

    # Use the existing vowel dictionary to calculate consonants
    consonant = {name: len(name) - vowel[name] for name in names}
    # Filter the vowel dictionary to include only keys that start with a vowel
    vowel = {key: value for key, value in vowel.items() if key[0].lower() in VOWELS}

    # Filter the vowel dictionary to include only keys that do NOT start with a vowel
    consonant = {key: value for key, value in consonant.items() if key[0].lower() not in VOWELS}

    return {'consonant': consonant, 'vowel': vowel}


# Test names
names = ("Alice", "John", "Lisa", "John", "Eric", "Waldo", "annie", "Alice", "John")

# Call the function and print the result
print(name_mapping(names))
expected = {
    "consonant": {"John": 3, "Waldo": 1, "Lisa": 1},
    "vowel": {"Alice": 2, "annie": 1, "Eric": 1},
}
assert name_mapping(names) == expected
print("First ok!")

only_consonants = ("John", "Doe", "Doe")
expected2 = {"consonant": {"John": 1, "Doe": 2}}
assert name_mapping(only_consonants) == expected2
print("Second ok!")

assert name_mapping([]) == {}

print("All ok!")