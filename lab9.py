word_list = open("text.txt", encoding="latin-1").read().split()
word_count = {}
word_count[word] = 0 if word not in word_count else word_count[word]+1 for word in word_list


