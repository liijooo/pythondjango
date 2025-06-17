s="python is a programming language"
char='a'
count=s.count(char)
print(count)

s="python is a programming language"
words=s.split()
for i in words:
    if len(i)<5:
        print(i)


s="python is a programming language"
find=s.index('o')
print(find)