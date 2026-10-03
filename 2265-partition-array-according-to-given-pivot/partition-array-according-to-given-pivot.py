class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        lst_l=[]
        lst_h=[] 
        lst_m=[]
        for i in nums:
            if i==pivot:
                lst_m.append(i)


        for i in nums:
            if i<pivot:
                lst_l.append(i)
            elif i>pivot:
                lst_h.append(i)
        
        result=[]
        for i in lst_l:
            result.append(i)
        
        for j in lst_m:
            result.append(j)
        
        
        for k in lst_h:
            result.append(k)
        return result