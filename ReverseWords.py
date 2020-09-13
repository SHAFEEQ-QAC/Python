def reverseword(word):
	i=len(word)-1
	newword=""
	while i>=0:
		newword= newword + word[i]
		i-=1
	return newword


message=input("Enter any message")
newmessage=""
word=""
i=0
while i<len(message):
	if message[i]==" ":
		newmessage+=(" "+reverseword(word))
		word=""		
	else:
		word+=message[i]
	i+=1
print(newmessage)