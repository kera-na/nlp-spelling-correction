from dictionary_service import DictionaryManager


def main() -> None:
    dm = DictionaryManager()

    # Test 1 - Prefix search
    print("Test 1 - Prefix search (bio):")
    print(dm.get_matches("bio"))

    # Test 2 - Substring search
    print("Test 2 - Substring search (virus):")
    print(dm.search_substring("virus"))

    # Test 3 - Valid word check (should return True)
    print("Test 3 - Valid word check (virus):")
    print(dm.is_word_valid("virus"))

    # Test 4 - Invalid word check (should return False)
    print("Test 4 - Invalid word check (xyzabc):")
    print(dm.is_word_valid("xyzabc"))


if __name__ == "__main__":
    main()
