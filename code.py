#20161027
#言語:python3
import math

a = [1,2,3,4,5,6,7,8,9,10,11,12,13]
left = 0
right = int(len(a))

#探索する文字列
serch = 13
to = 0

while left < right:
	mid = int((left + right)/2)
	if a[mid] == serch:
		print("左から"+str(mid+1)+"番目にあります")
		to = 1
		break
	elif serch < a[mid]:
		right = mid
	else:
		left = mid + 1
if to == 0:
	print("見つかりませんでした")
