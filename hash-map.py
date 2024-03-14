class HashMap:
    def __init__(self):
        self.data = []

    def add(self, key, value):
        for item in self.data:
            if item[0] == key:
                item.append(value)
                return
        self.data.append([key, value])

    def get(self, key):
        for item in self.data:
            if item[0] == key:
                return item[1]
        return None

    def contains(self, key):
        for item in self.data:
            if item[0] == key:
                return True
        return False

    def remove(self, key):
        for i, item in enumerate(self.data):
            if item[0] == key:
                del self.data[i]
                return
        return None

    def __iter__(self):
        return iter(self.data)


# Create a hash map
my_hash_map = HashMap()

# Add some elements to the hash map
my_hash_map.add("name", "Alice")
my_hash_map.add("age", 25)

# Get the value for a key
print(my_hash_map.get("name"))  # Alice

# Check if a key exists in the hash map
print("age" in my_hash_map)  # True
print("city" in my_hash_map)  # False

# Remove an element from the hash map
my_hash_map.remove("age")
my_hash_map.add("name", "Bob")

# Iterate over the hash map
# for key, value in my_hash_map:
#     print(key, value)
my_hash_map.add("age",22)
my_hash_map.add("age",23)
print(my_hash_map.data)