# Import necessary libraries
# TextBlob is used for spell correction and simple NLP operations
# LanguageTool is used for grammar and style checking
from textblob import TextBlob
from language_tool_python import LanguageTool

# Spell Checking (.correct() method)
# Recommended limit: ~100–200 words per call.

# Language_tool_python
# Used for grammar (.check() method)
# 20,000 characters (~3000 words) per check.
class SpellCheckerModule:
    def __init__(self):
        # Initialize the TextBlob and LanguageTool instances
        # TextBlob will handle spell correction (though initialized empty here)
        # LanguageTool is initialized for English (US) grammar checking
        self.spell_check = TextBlob("")
        self.grammar_check = LanguageTool('en-US')

    def correct_spell(self, text):
        """
        Corrects spelling mistakes in the given text using TextBlob.
        """

        # Example: "Helo World subscribe to my channel"
        # After split(): ['Helo', 'World', 'subscribe', 'to', 'my', 'channel']
        words = text.split()  # Split text into words (list of strings)

        corrected_words = []  # To store the corrected words

        # Iterate through each word and correct it
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            # TextBlob.correct() returns a Word object, so we convert it to string
            corrected_words.append(corrected_word)

        # Join corrected words back into a sentence
        return " ".join(corrected_words)

    def correct_grammar(self, text):
        """
        Detects grammatical errors in the given text using LanguageTool.
        Returns a list of rule IDs for the detected mistakes.
        """
        """
        Stores the words with grammatical mistakes and style errors
        in the form of object Match 
        """
        # Check the text for grammar and style issues
        matches = self.grammar_check.check(text)
        # Each element in 'matches' is a Match object describing a specific issue
        # (like subject-verb agreement, punctuation, style, etc.)

        found_mistakes = []  # To store detected rule IDs
        # corrected_sentence = self.grammar_check.utils.correct(text, matches)
        # Extract rule IDs from each Match object
        for mistake in matches:
            found_mistakes.append(mistake.ruleId)

        # Return list of grammar or style rule identifiers found
        return found_mistakes
