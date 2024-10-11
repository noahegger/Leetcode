# First Attempt explanation:
# Set target = 0, initialize triplets as empty set
# Iterate through i, x
# For a given x, new_target = -x -> now two-sum problem
# Iterate through j, y != i, x
# Set the complement (z) = new_target - y= -x -y
# Iterate through k, z != j and != i
# If z == comp, add indices (because unique) to triplets, [i, j, k]
# Sort each list in triplets, set(t.sort for t in triplets)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0 # x + y + z = 0
        nums.sort()
        triplets = []
        for i in range(len(nums)-2): # initial x doesn't need to cover last two elements
            if i > 0 and nums[i] == nums[i-1]:
                continue # avoid duplicate
            new_target = -nums[i]
            # Use two pointer to look at remaining window
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == new_target:
                    triplets.append([nums[i], nums[l], nums[r]]) # append list if we found solution
                    l += 1 
                    r-= 1 # Increment search

                    while l < r and nums[l] == nums[l-1]: # skip potential duplicated
                        l+=1
                    while l < r and nums [r] == nums[r+1]:
                        r -= 1
                elif nums[l] + nums[r] < new_target:  #since sorted, increment l forward
                    l+= 1
                else:
                    r -= 1
        return triplets
                

           
                            
