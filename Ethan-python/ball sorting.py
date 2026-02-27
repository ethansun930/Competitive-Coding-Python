def ball_sort(nums:list[int]):
    n = len(nums)
    f = 0
    l = n-1
    i = 0
    while i < l + 1:
        if nums[i] == 0:
            nums[i], nums[f] = nums[f], nums[i]
            f += 1
            i += 1
        elif nums[i] == 1:
            i += 1
        else:
            nums[i], nums[l] = nums[l], nums[i]
            l -= 1
    print(nums)
    
#ball_sort([0,0,0,1,1,1,2,2,2])
# ball_sort([0,2,1,0,2,2,0,1,0])
ball_sort([0,0,0,0,2,1,1,2,1,2,1,2,0])