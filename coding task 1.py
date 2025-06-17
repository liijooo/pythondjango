sentence=input('enter the sentence')
words=sentence.split()
result={}
for i in words:
    if i not in result:
        word_length=len(i)
        rev_word=i[::-1]
        palindrome=i==rev_word
        count=i.count(i)

        result[i]={'length':word_length,'palindrome':palindrome,'count':count}

print(result)
