#讀檔
data = []
with open("reviews.txt","r") as f:
	for line in f:
		data.append(line)

print(data[0])

data_len = len(data)

lenth = 0
for line in data:
	lenth += len(line)
lenth_ave = lenth / data_len
print(lenth_ave)
#篩選有good的留言
good = []

for d in data:
	if "good" in d:
		good.append(d)

print("包含good的留言有", len(good), "筆")
print(good[0])

#快寫法
good = [d for d in data if "good" in d ]
print("包含good的留言有", len(good), "筆")

bad = ["bad" in d for d in data]
print(bad)


#文字計數
wc ={} #word count
for d in data:
	words = d.split(" ")
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc [word] > 1000000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input("你想查什麼字")
	if word == "q":
		break
	if word in wc:
		print(word, "出現的次數為", wc[word])
	else:
		print("沒出現過")

print("感謝你使用此功能")


