#讀檔
data = []
with open("reviews.txt","r") as f:
	for line in f:
		data.append(line)
data_len = len(data)

lenth = 0
for line in data:
	lenth += len(line)
lenth_ave = lenth / data_len
print(lenth_ave)

good = []
for d in data:
	if "good" in d:
		good.append(d)

print("包含good的留言有", len(good), "筆")
print(good[0])