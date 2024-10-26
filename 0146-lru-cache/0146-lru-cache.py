# My first thought naturally is to use a hash table
# In 3.7 onward, hash tables remember order

# In the absence of an ordered hash table,
# Linked lists seem to be the 
# way to go, given that we can move the
# recently accessed item to the top of the
# list, thus rendering the least recently
# used to the bottom

# Final gotcha: It will take O(n) to find
# and retrieve items by key w/ linked lists
# so we need to ~combine~ linked lists
# w/ hashmap

# I think the cleanest implementation
# is just to rely on the ordered hash table

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache[key] = self.cache.pop(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)

        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.pop(next(iter(self.cache)))
 


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)