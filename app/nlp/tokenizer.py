import re


class Tokenizer:
    def __init__(self):
        # Define regex patterns for specific token types
        self.patterns = {
            "MEASURE": r"\d+[\.,]?\d*\s*(?:ft|m|kg|s|²|³)",  # Numbers with units (e.g., 10,200 ft, 5.5 kg)
            "DATE": r"\d{1,4}[/-]\d{1,2}[/-]\d{1,4}",  # Dates (e.g., 2023-10-05, 05/10/2023)
            "CARDINAL": r"\d+",  # Cardinal numbers (e.g., 75, 124)
            "DECIMAL": r"\d+\.\d+",  # Decimal numbers (e.g., 3.14, 0.5)
            "ORDINAL": r"\d+(st|nd|rd|th)",  # Ordinal numbers (e.g., 1st, 2nd)
            "TIME": r"\d{1,2}:\d{2}(?::\d{2})?",  # Time (e.g., 12:30, 23:59:59)
            "MONEY": r"\$\d+[\.,]?\d*",  # Money (e.g., $10.50, $1,000)
            "TELEPHONE": r"\+?\d[\d\s-]{6,}\d",  # Telephone numbers (e.g., +1 234 567 890)
            "ELECTRONIC": r"\w+@\w+\.\w+",  # Email addresses (e.g., example@domain.com)
            "FRACTION": r"\d+/\d+",  # Fractions (e.g., 1/2, 3/4)
            "VERBATIM": r'"[^"]+"',  # Quoted text (e.g., "example")
            "PLAIN": r"\w+(?:-\w+)*",  # Plain words (e.g., free-webapp)
            "PUNCT": r"[^\w\s]",  # Punctuation (e.g., .,!?()²)
        }

    def tokenize(self, sentence):
        """
        Tokenizes a sentence into tokens, handling punctuation, special characters, and edge cases.
        """
        # Combine all patterns into a single regex
        combined_pattern = "|".join(f"(?P<{name}>{pattern})" for name, pattern in self.patterns.items())
        combined_regex = re.compile(combined_pattern, re.VERBOSE)

        # Find all matches in the sentence
        tokens = []
        for match in combined_regex.finditer(sentence):
            token = match.group().strip()  # Remove leading/trailing whitespace
            tokens.append(token)

        return tokens
