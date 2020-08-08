data = []
count = 0
count1 = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1
		data.append(line)
		if count % 100000 == 0:
			print(len(data))
print('檔案讀取完畢,總共有', len(data), '筆資料。')

sum_len = 0
for d in data:
	sum_len += len(d)
avg = sum_len / len(data)
avg = int(avg)
print('平均留言長度為', avg, '個字元。')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')

#print(line.strip())