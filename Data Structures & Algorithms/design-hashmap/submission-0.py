class MyHashMap:

    def __init__(self):
        self.obj = [[] for _ in range(10)]

    def put(self, key: int, value: int) -> None:

        for idx, item in enumerate(self.obj[key % 10]):
            if item[0] == key:
                self.obj[key % 10][idx] = (key, value)
                return
        self.obj[key % 10].append((key, value))

    def get(self, key: int) -> int:
        match = [item for item in self.obj[key % 10] if item[0] == key]
        if match: # non-empty list is true
            return match[0][1]
        else:
            return -1

    def remove(self, key: int) -> None:
        for idx, item in enumerate(self.obj[key % 10]):
            if item[0] == key:
                self.obj[key % 10].pop(idx)
                return
                


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)