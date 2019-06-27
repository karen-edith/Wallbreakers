class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'AaEeIiOoUu'
        vowelPositions = []
        inputString = list(s)

        for i in range(len(s)):
            if (s[i] in vowels):
                vowelPositions.append(i)

        if (len(vowelPositions) % 2 == 0):
            middle = len(vowelPositions)/2
            for j in range(len(vowelPositions)):
                if (j <= middle):
                    inputString[vowelPositions[j]] = s[vowelPositions[len(vowelPositions) - (j+1)]]
                    inputString[vowelPositions[len(vowelPositions) - (j+1)]] = s[vowelPositions[j]]
        else:
            middle = len(vowelPositions)/2
            for m in range(len(vowelPositions)):
                if (m < middle):
                    inputString[vowelPositions[m]] = s[vowelPositions[len(vowelPositions) - (m+1)]]
                    inputString[vowelPositions[len(vowelPositions) - (m+1)]] = s[vowelPositions[m]]

        return ''.join(inputString)
        
