def ascending_order(nums):
    for i in range(len(nums)):
        x = i
        for j in range(i+1, len(nums)):
            if nums[x] > nums[j]:
               x=j
           
        nums[i],nums[x] = nums[x],nums[i]
    print(nums)
y = [23,53,2,4,8,98,1,298,6]
z = [33,2,5,7,87,9,432,1]
ascending_order(y)
ascending_order(z)
