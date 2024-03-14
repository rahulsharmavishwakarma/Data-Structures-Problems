class HashSet:
    def __init__(self):
        self.data = []

    def add(self, element):
        for item in self.data:
            if item == element:
                return
        self.data.append(element)

    def contains(self, element):
        for item in self.data:
            if item == element:
                return True
        return False

    def remove(self, element):
        for i, item in enumerate(self.data):
            if item == element:
                del self.data[i]
                return
        return None

    def __iter__(self):
        return iter(self.data)


# Create a hash set
my_hash_set = HashSet()

# Add some elements to the hash set
my_hash_set.add(1)
my_hash_set.add(2)
my_hash_set.add(3)

# Check if an element is in the hash set
print(1 in my_hash_set)  # True
print(4 in my_hash_set)  # False

# Remove an element from the hash set
my_hash_set.remove(2)
my_hash_set.add(2)
# Iterate over the hash set
for element in my_hash_set:
    print(element)