s=input('enter the sentence')

words=s.split()
max_word=""
max_len=0

for i in words:
    if len(i)>max_len:
        max_len=len(i)
        max_word=i

print("the longest word is:",max_word)
print("length of the word is:",max_len)
