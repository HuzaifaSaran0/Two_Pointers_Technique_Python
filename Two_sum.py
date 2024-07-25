#The Question was: # Given a sorted array of integers nums and an integer target, return the indices of the two numbers such that they add up to the given target.

class Solution:
    # USING TWO POINTERS TECHNIQUE
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        num2 = nums.copy()
        num2.sort()

        while left < right:
            current_sum = num2[left] + num2[right]
            if current_sum == target:
                # Find the indices in the original array
                index1 = nums.index(num2[left])
                # To handle duplicates, remove the first found element to find the next
                nums[index1] = float('inf')  # Set the found index to an unreachable value
                index2 = nums.index(num2[right])
                return [index1, index2]
            elif current_sum > target:
                right -= 1
            else:
                left += 1

