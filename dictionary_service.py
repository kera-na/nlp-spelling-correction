from __future__ import annotations

import bisect
from pathlib import Path


class DictionaryManager:
    """Fast vocabulary lookup service for real-time GUI search."""

    def __init__(self, vocabulary_path: str | Path = "vocabulary.txt") -> None:
        self.vocabulary_path = Path(vocabulary_path)
        self.words = self._load_words()
        self._word_set = set(self.words)  # O(1) membership checks.

    def _load_words(self) -> list[str]:
        """Load vocabulary file into a sorted list without empty lines."""
        with self.vocabulary_path.open("r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]
        return sorted(words)

    def get_matches(self, query: str, mode: str = "prefix", limit: int = 50) -> list[str]:
        """
        Return up to `limit` matching words for `query`.

        Uses binary search to jump directly to the matching range, which keeps
        lookup fast for real-time search bars.
        """
        if not query:
            return self.words[:limit]

        if mode == "substring":  # FIX 3
            return [word for word in self.words if query in word][:limit]  # FIX 3
        if mode != "prefix":  # FIX 3
            raise ValueError("mode must be either 'prefix' or 'substring'")  # FIX 3

        prefix = query  # FIX 3
        start = bisect.bisect_left(self.words, prefix)
        end_prefix = prefix + "\uffff"
        end = bisect.bisect_right(self.words, end_prefix)
        return self.words[start:end][:limit]

    def search_substring(self, query: str, limit: int = 50) -> list[str]:
        """Convenience wrapper for substring matching."""  # FIX 3
        return self.get_matches(query, mode="substring", limit=limit)  # FIX 3

    def is_word_valid(self, word: str) -> bool:
        """Return True if word exists in the vocabulary."""
        return word in self._word_set
