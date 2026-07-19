class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1=[]
        for char in s:
            if char.isalnum():
                str1.append(char.lower())
        cleaned = "".join(str1)
        cleaned_rev = cleaned[::-1]
        return cleaned == cleaned_rev  