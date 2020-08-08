data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1
		data.append(line)
		if count % 100000 == 0:
			print(len(data))
print(len(data))
print(data[0])
#print(line.strip())