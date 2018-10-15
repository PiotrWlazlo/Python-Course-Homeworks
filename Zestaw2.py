#Python course homework - set of tasks no.2
#2.10
#count words in multiline string
line = "All the world's a stage,\
And all the men and women merely players;\
They have their exits and their entrances,\
And one man in his time plays many parts"
len(line.split())
#2.11
#underscore between chars
word = "eucalyptus"
str = ""
for i in word:
	str += i+"_"

print(str)
#2.12
#begin chars
words = line.split()
letters = [word[0] for word in words]
print("".join.letters)
#end chars
letters = [word[len(word)-1] for word in words]
print("".join.letters)
#2.13
#Total sum of chars in sentence
len("".join(words))
#2.14
#longest word
word = max(words, key=len)
len(word)
#2.15
L = [2,5,1,7,4]
L2 = [str(x) for x in L]
print("".join(L2))
#2.16
line.replace('GvR','Guido van Rossum')
#2.17
sorted(words)
sorted(words, key=len)
#2.18
x = 289102490593034920
x2 = str(x)
x2.count(0)
#2.19
L = [4,25,142,5,242,13,24]
result = [str(item).zfill(6) for item in L]
