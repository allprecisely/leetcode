# https://leetcode.com/problems/implement-trie-prefix-tree/description/

class Trie:

    def __init__(self):
        self.root = {}
        

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node[''] = ''

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if not node or c not in node:
                return False
            node = node[c]
        return '' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if not node or c not in node:
                return False
            node = node[c]
        return True
