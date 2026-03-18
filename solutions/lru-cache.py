class Node:

    def __init__(self):

        self.key = None
        self.value = None
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
 
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = {}
        self.capacity = capacity

    def remove(self, node): 

        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):

        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node

    def get(self, key: int) -> int:
        
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        
        else:
            node = Node()
            node.key = key
            node.value = value

            if len(self.cache) >= self.capacity:

                lru = self.head.next
                self.remove(lru)
                del self.cache[lru.key]
            
            self.cache[key] = node
            self.insert(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)