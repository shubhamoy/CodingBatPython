def max_end3(nums):
	c = nums[0] if nums[0] > nums[-1] else nums[-1]
	b = []
	for i in range(len(nums)):
		b.append(c)
	return b
