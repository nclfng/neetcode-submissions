class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        newS = list(s)
        newS.sort()
        newT = list(t)
        newT.sort()

        if len(newS) != len(newT):
            return False

        for i in range(len(newS)):
            if newS[i] != newT[i]:
                return False
        
        return True