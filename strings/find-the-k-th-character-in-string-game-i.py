# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        n = 1

        while n < k:
            for char in word:
                next_char_ascii = ord(char) + 1
                next_char = chr(97 + ((next_char_ascii - 97) % 26))

                word += next_char
            n = len(word)

        return word[k-1] #0 indexing
