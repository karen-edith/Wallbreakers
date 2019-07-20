class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def backtracking(index, current, ans):
            if current == target:
                answer.append(ans)
                return
            if current > target:
                return
            i = index
            while i < len(candidates):
                backtracking(i, current + candidates[i], ans + [candidates[i]])
                while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                    i += 1
                i += 1
        backtracking(0, 0, [])
        return answer
