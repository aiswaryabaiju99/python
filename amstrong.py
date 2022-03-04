# # a=123
# # b=a%10
# # print(b

# a=124
# b=a//10
# print(b)
# 124
# 4
# 12
a=153
s=a
d=0
while(a>0):
	b=a%10
	b=b*b*b
	d=d+b
	a=a//10
	print(d)
	print(s)
if d==s:
	print("armstrong")
else:
	print("not armstrong")


	


	
