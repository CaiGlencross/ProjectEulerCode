def evenFibSum(n):
	prev=1
	cur=1
	evenSum=0
	while cur<n:
		if (prev+cur)%2==0:
			evenSum+=(prev+cur)
		nxt=cur+prev
		prev=cur
		cur=nxt

	return evenSum

print evenFibSum(4000000)

