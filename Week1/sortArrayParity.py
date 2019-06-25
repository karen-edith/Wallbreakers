class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        B = []
        C = []

        if len(A) == 1:
            return A
        else:
            for x in A:
                if(x % 2 == 0):
                    B.append(x)
                else:
                    C.append(x)
            return (B + C)
