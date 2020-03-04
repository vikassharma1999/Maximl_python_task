'''
Name: Vikas Sharma
Id: 201752041
'''

def check(ls,max_):
	t=0
	for i in range(26):
		if(ls[i]):
			t+=1
	return (t==max_)


print("Enter the string....\n")
str_ = input() 
n = len(str_)  
ls = [0]*30  
for i in range(n):
	ls[ord(str_[i])-ord('a')]=1
max_=0
ans = 1
for i in range(26):
	max_+=ls[i]
low=1
high=n
while(low<=high):
	mid=(low+high)//2
	f=[0]*30
	flag=0
	for i in range(mid):
		f[ord(str_[i])-ord('a')]+=1
	for j in range(1,n-mid+1):
		if(check(f,max_)):
			flag=1
			break

		f[ord(str_[j-1])-ord('a')]-=1
		f[ord(str_[j+mid-1])-ord('a')]+=1

	if(check(f,max_)):
		flag=1
	if(flag):
		ans=mid
		high=mid-1
	else:
		low=mid+1

print("The result is....\n")
print(ans)