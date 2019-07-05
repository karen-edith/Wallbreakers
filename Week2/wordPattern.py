class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        # setup empty letter dictionary to create s[i]-word map
        patternMap = {}
        # split each word in str and place into array
        stringArray = str.split()

        # if both pattern and stringArray are empty they do not have the same pattern
        if len(pattern) == 0 and len(stringArray) == 0:
            return True

        # if pattern and string Array have different lengths they do not have same pattern
        if len(pattern) != len(stringArray):
            return False

        # place new letter-word pair in patternMap
        for i in range(len(pattern)):
            # check to see if key pattern[i] part of patternMap
            if pattern[i] not in patternMap:
                # if not, check to see if corresponding stringArray value is mapped to a different key
                if stringArray[i] in patternMap.values():
                    # if mapped to a different key then string pattern and str do not have the same pattern
                    return False
                patternMap[pattern[i]] = stringArray[i]

           # if key does exist check to see if key has been mapped to a different value
            else:
                if patternMap[pattern[i]] != stringArray[i]:
                    # if it has been mapped to a different value then
                    # str and pattern do not share a similar order
                    return False

        return True
