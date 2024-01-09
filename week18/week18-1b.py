a = int(input())
if a<2000:
	print('100')
else:
	ans=(a-2000)//500*5+100
	if (a-2000)//500!=0:
		ans+=5
print(ans)