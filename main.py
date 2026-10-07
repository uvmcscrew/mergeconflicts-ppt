from BloomFilter import BloomFilter

bloom_filter = BloomFilter()

bloom_filter.add("layla")
bloom_filter.add("ruth")
bloom_filter.add("gregory")
bloom_filter.add("raine")
bloom_filter.add("atticus")

print(bloom_filter.has("cscrew"))
print(bloom_filter.has("raine"))
