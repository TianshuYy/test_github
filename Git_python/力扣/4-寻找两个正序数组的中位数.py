def findMedianSortedArrays(nums1,nums2):
    nums=nums1+nums2
    nums.sort()
    nums_len=len(nums)
    if nums_len%2==0:
        index1=int((nums_len/2)-1)
        index2=int((nums_len/2))
        return (nums[index1]+nums[index2])/2
    else:
        index=int(nums_len/2)
        return nums[index]
num1=[1,2]
num2=[3,4]
print(findMedianSortedArrays(num1, num2))