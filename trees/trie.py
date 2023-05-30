class TreeNode:
    def __init__(self):
        self.children = [None] * 26  # 26 alphabets
        self.is_end_of_word = False


class Trie:
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        # returns new Trie Node
        return TreeNode()

    def _char_to_index(self, ch):
        # converts key current character into index
        # use only 'a' to 'z' and lower case
        return ord(ch) - ord('a')

    def insert(self, key):
        # If not present, insert the key into Trie
        # If the key is prefix of trie node, just marks leaf node
        p_crawl = self.root
        length = len(key)
        for level in range(length):
            index = self._char_to_index(key[level])

            # If current character not present
            if not p_crawl.children[index]:
                p_crawl.children[index] = self.getNode()
            p_crawl = p_crawl.children[index]

        # mark last node as leaf node
        p_crawl.is_end_of_word = True

    def search(self, key):
        p_crawl = self.root
        for level in range(len(key)):
            index = self._char_to_index(key[level])
            if not p_crawl.children[index]:
                return False
            p_crawl = p_crawl.children[index]
        return p_crawl.is_end_of_word


if __name__ == '__main__':
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the"]#, "a", "there", "anaswe", "any",
            #"by", "their"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    # print("{} ---- {}".format("these", output[t.search("these")]))
    # print("{} ---- {}".format("their", output[t.search("their")]))
    # print("{} ---- {}".format("thaw", output[t.search("thaw")]))
