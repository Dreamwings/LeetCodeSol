class MagicDictionary:

    def __init__(self):
        
        self.d = collections.defaultdict(set)
        
    def buildDict(self, dictionary: List[str]) -> None:
        
        for word in dictionary:
            for i in range(len(word)):
                w = word[:i] + '*' + word[i+1:]
                self.d[w].add(word)        

    def search(self, searchWord: str) -> bool:
        
        for i in range(len(searchWord)):
            w = searchWord[:i] + '*' + searchWord[i+1:]
            if w in self.d:
                if searchWord not in self.d[w]:
                    return True
                elif len(self.d[w]) > 1:
                    return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)