class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        node = self.root

        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True


    def _dfs(self, node, prefix, results, limit):
        if len(results) >= limit:
            return

        if node.is_end:
            results.append(prefix)

        for char, next_node in node.children.items():
            self._dfs(next_node, prefix + char, results, limit)


    def autocomplete(self, prefix, limit=5):
        node = self.root

        for char in prefix.lower():
            if char not in node.children:
                return []

            node = node.children[char]

        results = []

        self._dfs(node, prefix.lower(), results, limit)

        return results



words = []

with open("word.txt", "r") as file:
    for line in file:
        words.append(line.strip())



trie = Trie()

for word in words:
    trie.insert(word)


print("Autocomplete system")


while True:
    print("\033[0m", end="")
    prefix = input("початок слова: ")

    if prefix.lower() == "exit":
        break

    suggestions = trie.autocomplete(prefix)

    if suggestions:
        print("\n:")

        for word in suggestions:
            print("-", word)

    else:
        print("\031\031[0m")

    print()