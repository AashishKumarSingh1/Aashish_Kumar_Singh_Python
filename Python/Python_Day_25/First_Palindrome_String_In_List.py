class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            rev_word=word[::-1]
            if word==rev_word:
                return word
        return ""