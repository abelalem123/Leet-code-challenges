# class Solution:
#     def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
#         for j in range(len(names)):
#             for i in range(1,len(names)-j):   
#                 if heights[i-1]<heights[i]:
#                     temp=names[i-1]
#                     names[i-1]=names[i]
#                     names[i]=temp
#                     tempn=heights[i-1]
#                     heights[i-1]=heights[i]
#                     heights[i]=tempn
#         return names

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hgts=sorted(heights,reverse=True)
        p=[]
        for i in hgts:
            p.append(names[heights.index(i)])
        return p