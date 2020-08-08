data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1
		data.append(line)
		if count % 100000 == 0:
			print(len(data))
print('檔案讀取完畢,總共有', len(data), '筆資料。')
#print(line.strip())