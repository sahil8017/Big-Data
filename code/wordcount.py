# WordCount using MapReduce concept

text = "big data analytics big data"

# MAP PHASE
words = text.split()

mapped = []

for word in words:
    mapped.append((word, 1))

print("Mapped Output:")
print(mapped)

# REDUCE PHASE
reduced = {}

for word, count in mapped:
    if word in reduced:
        reduced[word] += count
    else:
        reduced[word] = count

print("\nReduced Output:")
print(reduced)