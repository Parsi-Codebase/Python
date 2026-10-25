# Implementing a Simple Hash Table (Manually)
# Custom simple hash table implementation

class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]  # buckets
    # Simple hash function
    def _hash(self, key): 
        return hash(key) % self.size  # hash function
    def insert(self, key, value):
        index = self._hash(key)
        # Handle collision (chaining)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
    
    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # not found
    
    def display(self):
        for i, bucket in enumerate(self.table):
            print(i, ":", bucket)


# Using our HashTable
h = HashTable()
h.insert("name", "Akhil")
h.insert("age", 25)
h.insert("city", "Hyderabad")
h.insert("email", "akhil@example.com")

h.display()

print("Get city:", h.get("city"))

    