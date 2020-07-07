word = input()
word = word.upper()
wordlist = [0]*26
for i in word:
    wordlist[ord(i)-65] += 1
answer = chr(wordlist.index(max(wordlist))+65)
wordlist = sorted(wordlist,reverse=True)
if wordlist[0]==wordlist[1]:
    answer = '?'
print(answer)