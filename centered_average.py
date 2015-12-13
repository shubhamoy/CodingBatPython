def centered_average(nums):
	nums.pop(nums.index(max(nums)))
	nums.pop(nums.index(min(nums)))
	r = 0
	for i in range(len(nums)):
		r += nums[i]
	return int(r/len(nums))
