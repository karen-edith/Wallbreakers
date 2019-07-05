class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #initializing MyHashMap as an empty string array of length 100000
        self.hmap = [''] * 100000

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # place value in key index of hmap array
        self.hmap[key] = value


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        # if key index of hmap array contains an empty string then key value
        # hasn't been used again
        if (self.hmap[key] == ''):
            return -1
        # if key index of hmap array contains a value, return that value
        else:
            return self.hmap[key]


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        # to remove key value mapping, set key index to empty string
        self.hmap[key] = ''
