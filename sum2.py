def sum2(nums):
	if len(nums) == 0:
		return 0
	if len(nums) == 1:
		return nums[0]
	if len(nums) == 2:
		return nums[0]+nums[-1]
	elif len(nums) > 2:
		return nums[0]+nums[1]
