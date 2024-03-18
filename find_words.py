class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.refs = 0

    def add_word(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.is_end = True

    def rm_word(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add_word(word)

        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                board[r][c] not in node.children or
                node.children[board[r][c]].refs < 1 or
                (r, c) in visited
            ):
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.is_end:
                node.is_end = False
                res.add(word)
                root.rm_word(word)

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
