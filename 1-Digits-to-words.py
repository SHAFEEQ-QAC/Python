

ones=["","one","two","Three","Four","Five","six","seven","egiht","nine","ten"," eleven"," tweleve"," thirteen","forteen","fifteen","sixteen","seventeen","eighteen","ninteen"]
ty=["",""," Twenty"," Thirty"," forty"," fifty"," sixty"," seventy"," eighty"," ninty"]
num=int(input("Enter any number "))
Answer=""
if num>=1000 and num<=9999:
	Answer+=ones[int(num/1000)] + " thousand ";
	num-=int(num/1000)*1000
if num>=100 and num<1000:
	Answer+= ones[int(num/100)] + " Hundred"
	num-=int(num/100)*100
if num>=20 and num<100:
	Answer+=ty[int(num/10)]
	num-=int(num/10)*10
if num<=19:
	Answer+=ones[num]

print(Answer)