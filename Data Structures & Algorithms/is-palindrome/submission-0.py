class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1=[]
        for char in s:
            if char.isalnum():
                str1.append(char)
        cleaned = "".join(str1).lower()
        cleaned_rev = cleaned[::-1]
        if cleaned == cleaned_rev:
            return True
        else:
            return False    