from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # before starting counter, check to make sure that first Value is 5
        # otherwise you won't have exact change to give back
        if (bills[0] != 5):
            return False

        # set up bill counter and set first counter value
        counter = defaultdict(int)
        counter[bills[0]] = counter[0] + 1

        # start from second person
        for i in range(1, len(bills)):
            # 5 dollar bilss get counted right away, no change needed
            if bills[i] == 5:
                counter[5] = counter[5] + 1
            # 10 dollar bills get counted only if 5 dollar bills are available
            # if 5 dollar bills are availbale then take away one 5 dollar bill
            # and add count the 10 dollar bill
            elif bills[i] == 10 and counter[5] != 0:
                counter[5] = counter[5] - 1
                counter[10] = counter[10] + 1
            # if 10 dollar bill give and no 5 dollar bills available, no exact
            # change can be given
            elif bills[i] == 10 and counter[5] == 0:
                return False
            # 20 dollar bills require 15 dollar change (this begins the greedy
            # algorithm)
            elif bills[i] == 20:
                dueChange = 15
                while dueChange > 0:
                    # if 10 dollars are available, use those up first
                    # then if 5 dollar bills are available use those up afterwards
                    if dueChange >= 10 and counter[10] != 0:
                        counter[10] = counter[10] -1
                        dueChange = dueChange - 10
                    # if only 5 dollar bills exist, use them
                    elif counter[5] != 0:
                        counter[5] = counter[5] - 1
                        dueChange = dueChange - 5
                    # if none of the above cases is true, there isnt enough exact change
                    else:
                        return False
            # if the loop makes it to the end without returning a false, then it
            #there must've been enough change for all customers
            if i == len(bills) - 1:
                return True
