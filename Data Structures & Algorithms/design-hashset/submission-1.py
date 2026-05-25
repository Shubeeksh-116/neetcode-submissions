class MyHashSet:

    def __init__(self):
        self.h = []

    def add(self, key: int) -> None:
        if key not in self.h:
            self.h.append(key)
        print(self.h)

    def remove(self, key: int) -> None:
        if key in self.h:
            self.h.remove(key)
        print(self.h)

    def contains(self, key: int) -> bool:
        if key in self.h:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)