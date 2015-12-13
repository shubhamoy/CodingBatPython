def reverse3(nums):
	b=[]
	for i in range(len(nums)-1, 0, -1):
		b.append(nums[i])
	b.append(nums[0])
	return b
