# Unique Morse Code Words #
# https://leetcode.com/problems/unique-morse-code-words/description/

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_mapping = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
                         'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
                         'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',
                         'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}

        morse_set = set()
        for word in words:
            morse_word = ""
            for letter in word:
                morse_word = morse_word + morse_mapping[letter]
            morse_set.add(morse_word)
        return (len(morse_set))