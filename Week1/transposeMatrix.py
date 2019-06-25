class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        row = [];
        transposedArray = [];

        print(len(A))

        if len(A) == 1 and len(A[0]) == 1:
            return A
        else:
            for i in range(len(A[0])):
                for j in range(len(A)):
                    row.append(A[j][i])
                transposedArray.append(row)
                row = []
            return transposedArray
    
