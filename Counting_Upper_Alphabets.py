
Alpha=[0]*26
message=input("Enter a message")
a=0
while a<len(message):
	Alpha[ord(message[a:a+1])-65]=Alpha[ord(message[a:a+1])-65]+1
	a=a+1

i=0
while i<=25:
	if Alpha[i]!=0:
		print( chr(i+65),"--",Alpha[i])
	i=i+1