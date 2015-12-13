def rotate_left3(nums):
	b=[]
	for i in range(len(nums)-1):
		b.append(nums[i+1])
	b.append(nums[0])
	return b
