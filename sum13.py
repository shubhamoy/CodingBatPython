def sum13(nums):
	s=0
	if len(nums) == 0:
		return 0
	for i in range(len(nums)):
		if nums[i] != 13 and nums[i-1] != 13:
			s += nums[i]
	if nums[len(nums)-1]==13 and nums[0] != 13:
		s += nums[0]
	return s
