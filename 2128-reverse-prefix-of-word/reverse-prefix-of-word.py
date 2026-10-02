class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i=0
        result=""
        try:
            while word[i]!=ch:
                result+=word[i]
                i+=1
            result += word[i] 
            return result[::-1]+word[i+1:]
        except IndexError:
            return word