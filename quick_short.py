def quick_short(nums):
    if len(nums) <= 1:
        return nums
    
    pivot = nums[len(nums)-1]

    st = -1
    nt = 0

    while nt < len(nums)-1:
        if nums[nt] < pivot:
            st += 1
            nums[st], nums[nt] = nums[nt], nums[st]
        nt += 1
    nums[st+1], nums[len(nums)-1] = nums[len(nums)-1], nums[st+1]
    left = quick_short(nums[:st+1])
    right = quick_short(nums[st+2:])
    return left + [nums[st+1]] + right


if __name__ == "__main__":
    list = [5,3,6,2,10,1,4]
    print(quick_short(list))