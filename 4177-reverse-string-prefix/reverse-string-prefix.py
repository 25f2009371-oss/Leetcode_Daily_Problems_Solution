class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        res_lst=s[k::]
        res_first=""
        for i in range(k):
            res_first+=s[i]
        res_first=res_first[::-1]
        result=res_first+res_lst
        return result

