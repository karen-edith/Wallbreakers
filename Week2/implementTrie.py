class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = dict()
        self._end = '*'

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if len(self.trie) == 0:
            tempTrie = self.trie
            for letter in word:
                tempTrie = tempTrie.setdefault(letter, {})
            tempTrie[self._end] = self._end
        else:
            tempTrie = self.trie
            for letter in word:
                if letter in tempTrie:
                    tempTrie = tempTrie[letter]
                else:
                    tempTrie = tempTrie.setdefault(letter, {})
            tempTrie[self._end] = self._end

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.

        """
        tempTrie = self.trie
        for letter in word:
            if letter in tempTrie:
                tempTrie = tempTrie[letter]
            else:
                return False
        else:
            if self._end in tempTrie:
                return True
            else:
                return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tempTrie = self.trie
        for i in range(len(prefix)):
            if prefix[i] in tempTrie:
                tempTrie = tempTrie[prefix[i]]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
#obj = Trie()
#obj.insert('apple')
#param_2 = obj.search('apple')
# param_3 = obj.startsWith(prefix)
