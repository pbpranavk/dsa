class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = self.get_node()


    def get_node(self):
        return TrieNode()

    def _char_to_index(self, ch):
        return ord(ch) - ord("a")

    def insert(self, key):
        p_crawl = self.root
        length = len(key)

        for level in range(length):
            index = self._char_to_index(key[level])

            if not p_crawl.children[index]:
                p_crawl.children[index] = self.get_node()
            p_crawl = p_crawl.children[index]
        p_crawl.is_end_of_word = True

    def search(self, key):
        p_crawl = self.root
        length = len(key)

        for level in range(length):
            index = self._char_to_index(key[level])
            if not p_crawl.children[index]:
                return False
            p_crawl = p_crawl.children[index]

        return p_crawl.is_end_of_word

keys = ["the","a","there","anaswe","any", "by","their"]
output = ["Not present in trie", "Present in trie"]

t = Trie()

for key in keys:
    t.insert(key)

print("{} ---- {}".format("the",output[t.search("the")]))
print("{} ---- {}".format("these",output[t.search("these")]))
print("{} ---- {}".format("their",output[t.search("their")]))
print("{} ---- {}".format("thaw",output[t.search("thaw")]))