a, b=list(map(int,input().split()))
if a%b==0:
	print(a//b, end='')
if a%b !=0:
	print(a//b+1, end='')