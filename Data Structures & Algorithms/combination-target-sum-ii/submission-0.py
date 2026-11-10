class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # may contain dupes
        # return list of all unique combs of cands, chosen nums sum = target
        # chosen at most once, should know index bc dupes
        # use or dont use / move on

        output = []
        candidates.sort()

        def helper(index, currList):
            # base cases
            if sum(currList) == target:
                output.append(list(currList))
                return
            
            if index >= len(candidates) or sum(currList) > target:
                return

            currList.append(candidates[index])
            helper(index + 1, currList)
            
            currList.pop()
            skip = 1
            while index + skip < len(candidates):
                if candidates[index] == candidates[index + skip]:
                    skip += 1
                else:
                    break
            
            helper(index + skip, currList)
        
        helper(0, [])
        return output