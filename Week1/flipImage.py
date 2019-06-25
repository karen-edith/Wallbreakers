class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        B = [x[:] for x in A]

        if (len(A[0]) % 2 == 0):
            even = True
            midpoint = len(A)/2
        else:
            even = False
            midpoint = len(A)//2

        for x in range(len(A)):
            for y in range(len(A[x])):
                if (even == True and y <= midpoint - 1):
                    B[x][y] = A[x][len(A[x]) - (y + 1)]
                    B[x][len(A[x]) - (y + 1)] = A[x][y]
                elif (even == False and y < midpoint):
                    B[x][y] = A[x][len(A[x]) - (y + 1)]
                    B[x][len(A[x]) - (y + 1)] = A[x][y]
                elif (even == False and y == midpoint):
                    B[x][y] = A[x][y]


        for i in range(len(B)):
                for j in range(len(A[i])):
                    if(B[i][j] == 0):
                        B[i][j] = 1
                    else:
                        B[i][j] = 0
        return B
