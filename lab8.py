word_list = open("text.txt", encoding="latin-1").read().split()
word_count = {}
for word in word_list:
    if word not in word_count:
        word_count[word] = 0
    word_count[word] += 1

def top10(L):
    return sorted(L, reverse=True)[:10]
inv_map = {v: k for k, v in word_count.items()}

top10_inx = top10(inv_map)
top10_words = []
print(top10_inx)
for i in top10_inx:
    top10_words.append(inv_map[i])
print(top10_words)