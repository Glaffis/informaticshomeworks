class Box:
    def __init__(self, cat=None):
        self.cat = cat
        self.nextcat = None
        self.prevcat = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def _get_box(self, catIndex):
        if catIndex < 0 or catIndex >= self._size:
            raise IndexError("error")
        if catIndex < self._size // 2:
            box = self.head
            i = 0
            while i < catIndex:
                box = box.nextcat
                i += 1
        else:
            box = self.tail
            i = self._size - 1
            while i > catIndex:
                box = box.prevcat
                i -= 1
        return box

    def get(self, catIndex):
        box = self._get_box(catIndex)
        return box.cat
    def insert(self, catIndex, newcat):
        if catIndex < 0 or catIndex > self._size:
            raise IndexError("error")

        newbox = Box(newcat)

        if self._size == 0:
            self.head = newbox
            self.tail = newbox

        elif catIndex == 0:
            newbox.nextcat = self.head
            self.head.prevcat = newbox
            self.head = newbox

        elif catIndex == self._size:
            newbox.prevcat = self.tail
            self.tail.nextcat = newbox
            self.tail = newbox

        else:
            nextbox = self._get_box(catIndex)
            prevbox = nextbox.prevcat
            newbox.nextcat = nextbox
            newbox.prevcat = prevbox
            prevbox.nextcat = newbox
            nextbox.prevcat = newbox
        self._size += 1
    def remove(self, catIndex):
        if catIndex < 0 or catIndex >= self._size:
            raise IndexError("error")

        box_to_remove = self._get_box(catIndex)
        
        if box_to_remove.prevcat is not None:
            box_to_remove.prevcat.nextcat = box_to_remove.nextcat
        else:
            self.head = box_to_remove.nextcat

        if box_to_remove.nextcat is not None:
            box_to_remove.nextcat.prevcat = box_to_remove.prevcat
        else:
            self.tail = box_to_remove.prevcat

        self._size -= 1
    def addToEnd(self, newcat):
        self.insert(self._size, newcat)

    def contains(self, cat):
        current = self.head
        while current:
            if current.cat == cat:
                return True
            current = current.nextcat
        return False
    def LLprint(self):
        currentCat = self.head
        print("LINKED LIST")
        print("-----")
        i = 0
        while currentCat is not None:
            print(str(i) + ": " + str(currentCat.cat))
            i += 1
            currentCat = currentCat.nextcat
        print("-----")