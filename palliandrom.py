a=121
s=a
d=0
while(a>0):
	b=a%10
	d=d*10
	d=d+b
	
	a=a//10
	print(d)
if s==d:
	print("palliandrom")
else:
	print("not palliandrom")
	

	
