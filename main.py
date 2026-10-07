from BloomFilter import BloomFilter

bloom_filter = BloomFilter()

bloom_filter.add("henrik")
bloom_filter.add("ricky")
bloom_filter.add("hvt")
bloom_filter.add("unicycle guy")
bloom_filter.add("le frog")

print(bloom_filter.has("henrik"))
print(bloom_filter.has("test"))
