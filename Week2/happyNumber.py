class Solution:
    def isHappy(self, n: int) -> bool:
        # set up number dictionary and initialize digitSum
        number, digitSum = {}, 0

        # use while loop to iterate through n values until 1 is found
        while n != 1:
            digitSum, k = 0, n # set digitSum back to 0 before using again
            for i in str(n): # turn number into string to seperate digits
                # convert each digit back to integers and square it and add it to sum
                digitSum = digitSum + int(i)*int(i)
            n = digitSum # set new n value
            # check the new n against values of the number dictionary to see if it repeats
            for keys, value in number.items():
                if( n == value):
                    return False # if it does repeat we know it will never return 1
            number[str(k)] = n # place new n value in number dictionary
        return True
