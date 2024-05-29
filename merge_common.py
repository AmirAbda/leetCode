class Solution:
    def intersection(self, nums1, nums2):
        # Sort both arrays
        nums1.sort()
        nums2.sort()
        
        # Initialize two pointers
        p1, p2 = 0, 0
        result_set = set()  # Use a set to store unique elements
        
        # Traverse both arrays
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                result_set.add(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        
        # Convert the set to a list before returning
        return list(result_set)

# Example usage:
solution = Solution()
print(solution.intersection([1, 2, 2, 1], [2, 2]))  # Output: [2]
print(solution.intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [9, 4] or [4, 9]
