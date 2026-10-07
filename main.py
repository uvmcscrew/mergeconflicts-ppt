from BloomFilter import BloomFilter

bloom_filter = BloomFilter()

bloom_filter.add("alice")
bloom_filter.add("bob")
bloom_filter.add("carol")
bloom_filter.add("dan")
bloom_filter.add("erin")

print(bloom_filter.has("bob"))
print(bloom_filter.has("test"))
