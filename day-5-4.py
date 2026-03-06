nums1 = [35, 12, 97, 64, 55]
nums2 = []
for a in nums1:
    nums2.append(a ** 2)
print(nums2)

#列表生成式
#使用列表生成式创建列表不仅代码简单优雅，而且性能上也优于使用for-in循环和append方法向空列表中追加元素的方式。
nums3 = [num ** 3 for num in nums1]
print(nums3)