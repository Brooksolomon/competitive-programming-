class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
            x = 0
            y = 0
            while True:
                if y > n - 1:
                    break
                elif x > m-1:
                    nums1.pop()
                    nums1.insert(x,nums2[y])
                    x += 1
                    y += 1
                    continue
                if nums1[x] > nums2[y]:
                    nums1.pop()
                    nums1.insert(x, nums2[y])
                    y += 1
                    m += 1
                else:
                    x += 1
