from BloomFilter import BloomFilter

bloom_filter = BloomFilter()

bloom_filter.add("randy")
bloom_filter.add("mitchell")
bloom_filter.add("alphonso")
bloom_filter.add("raine")
bloom_filter.add("atticus")

print(bloom_filter.has("cscrew"))
print(bloom_filter.has("raine"))
