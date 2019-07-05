class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # set up an empty array
        self.set = []

    def add(self, key: int) -> None:

        # if key is not already in self.set array, place it in the array
        if key not in self.set:
            self.set.append(key)

    def remove(self, key: int) -> None:
        # if key is in self.set array then remove that value from array
        if key in self.set:
            self.set.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        # if key in self.set then arrary contains key otherwise it does not
        if key in self.set:
            return True
        else:
            return False
