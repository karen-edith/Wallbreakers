class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        # set up dictionary for alphabet morse map, list for Translation, and morseCodeWord string
        alphabetMorseMap, morseCodeTranslation, morseCodeWord = {}, [], ''

        # map the alphabet to corresponding morse code
        for i in range(len(morse)):
            asciiNum = i + ord('a')
            char = chr(asciiNum)
            alphabetMorseMap[char] = morse[i]

        # use map to translate words in words array to morse code
        for j in words:
            for k in j:
                morseCodeWord = morseCodeWord + alphabetMorseMap[k]
            morseCodeTranslation.append(morseCodeWord)
            morseCodeWord = ''

        # use set to remove repeat morse code translations
        morseCodeTranslationSet = set(morseCodeTranslation)

        return len(morseCodeTranslationSet)
