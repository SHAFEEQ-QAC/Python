


def longestword(message):
	word=""
	longest=""
	i=0
	while i<=len(message):
		if message[i:i+1]==" " or len(message)==i:
			if len(word)>len(longest):
				longest=word
				word=""
		else:
			word+=message[i:i+1]
		i+=1
	print("longest Word is:" , longest)

message=input("Enter A message")
longestword(message)