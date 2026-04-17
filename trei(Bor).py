class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Bor:
    def __init__(self):
        self.root = Node()

    def search(self, word):
        cur = self.root
        for i in word:
            if i not in cur.children:
                return False
            cur = cur.children[i]
        return cur.is_end

    def insert(self, word):
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = Node()
            cur = cur.children[i]
        cur.is_end = True

    def delete(self, word):
        path = []
        cur = self.root
        for i in word:
            if i not in cur.children:
                return False
            path.append((cur,i))
            cur = cur.children[i]
        if not cur.is_end:
            return False
        cur.is_end = False
        for j, i in reversed(path):
            child = j.children[i]
            if not child.is_end and len(child.children) == 0:
                del j.children[i]
            else:
                break
        return True