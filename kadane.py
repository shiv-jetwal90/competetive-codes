def kadane():
	arr= [-2,-3,4,-1,-2,1,5,-3]
	sum = arr[0]
	c_sum=0
	max_sum=-99999999
	for i in range(1,len(arr)):
		sum+=arr[i]
		if sum>max_sum:
			max_sum=sum
		if c_sum<sum:
			c_sum=sum
		if sum<0:
			sum=0
	if c_sum==0:
		print(max(arr))
	return max_sum

print(kadane(), 'ans')