import math

epsilon = 0.05  # False positive tolerance
n = 5  # Estimated number of items in Bloom filter


# Based off my own Bloom filter implementation in TypeScript
# Python is not the best language for this...
class BloomFilter:
    storage = []

    # See https://en.wikipedia.org/wiki/Bloom_filter#Optimal_number_of_hash_functions
    m = math.ceil(-((n * math.log(epsilon)) / (math.log(2) ** 2)))
    k = math.ceil(-(math.log(epsilon) / math.log(2)))

    def add(self, element):
        """Add an item into the Bloom filter."""
        if len(self.storage) != self.m:  # Check if Bloom filter exists in storage
            self.allocate()

        indexes = self.get_indexes(element)
        for index in indexes:
            self.storage[index] = 1

    def has(self, element):
        """Checks if an item exists in the Bloom filter. Returns `False` if not in storage, `True` if in storage
        with a false positivity tolerance of `epsilon` per `n` items."""
        if len(self.storage) != self.m:  # Check if Bloom filter exists in storage
            self.allocate()
            return False

        indexes = self.get_indexes(element)
        for index in indexes:
            if self.storage[index] == 0:
                return False

        return True

    # See https://willwhim.wpengine.com/2011/09/03/producing-n-hash-functions-by-hashing-only-once/
    def get_indexes(self, element):
        """Generate indexes of an element using hashes."""
        (a, b) = self.double_hash(element)
        indexes = []
        for i in range(self.k):
            indexes.append((a + b * i) % self.m)
        return indexes

    def double_hash(self, element):
        """Return two hashes from an element for index use."""
        # Python's hash() function doesn't support seeding, this is a workaround
        return [hash(element), hash(element + "_seeded")]

    def allocate(self):
        """Populate the storage to all `0`s."""
        self.storage = [0] * self.m
