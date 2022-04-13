#TODO: Redo and re learn this
class TrieNode:
    def __init__(self):
        self.map = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        current = self.root
        for char in word:
            if char in current.map:
                current = current.map[char]
            else:
                new_node = TrieNode()
                current.map[char] = new_node
                current = new_node
        current.isWord = True

    def startswith(self, prefix):
        current = self.root
        for char in prefix:
            if char in current.map:
                current = current.map[char]
            else:
                return False
        return True

    def search(self, prefix):
        current = self.root
        for char in prefix:
            if char in current.map:
                current = current.map[char]
            else:
                return False
        return current.isWord

    def delete(self, word):
        return self._delete(word, 0, self.root)

    def _delete(self, word, i, current):
        if i == len(word):
            if not current.isWord:
                return False
            current.isWord = False
            return len(current.map) == 0
        char = word[i]
        if char not in current.map:
            return False
        next_node = current.map[char]
        should_delete_ref = self._delete(word, i+1, next_node)
        if should_delete_ref:
            del current.map[char]
            return len(current.map) == 0
        return False



def dfs(board, i, j, trie, prefix, output):
    m, n = len(board), len(board[0])
    if i < 0 or j < 0 or i >= m or j >= n:
        return

    tmp = board[i][j]
    new_prefix = prefix + tmp

    if not trie.startswith(new_prefix):
        return

    exists = trie.search(new_prefix)
    if exists:
        output.append(new_prefix)
        trie.delete(new_prefix)

    board[i][j] = '#'
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for x, y in dirs:
        dfs(board, i+x, j-y, trie, new_prefix, output)
    board[i][j] = tmp

class Solution:
    def findWords(self, board, words):
        m, n = len(board), len(board[0])

        trie = Trie()
        for word in words:
            trie.add_word(word)

        output = []
        for i in range(m):
            for j in range(n):
                dfs(board, i, j, trie, '', output)

        return output