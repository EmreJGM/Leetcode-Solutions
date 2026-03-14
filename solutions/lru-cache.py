#doing O(n) to start then will update with correct requirements

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.touch = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.touch += 1
            self.cache[key]["touch"] = self.touch
            return self.cache[key]["value"]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.touch += 1 

        if key in self.cache:
            self.cache[key]["value"] = value
            self.cache[key]["touch"] = self.touch  
            return
            
        if len(self.cache) >= self.capacity:
            least_key = None
            least_touch = float("inf")

            for k, v in self.cache.items():
                if v["touch"] < least_touch:
                    least_touch = v["touch"]
                    least_key = k
            
            del self.cache[least_key]

        self.cache[key] = {"value": value, "touch": self.touch}        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)