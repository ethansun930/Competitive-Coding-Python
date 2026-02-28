"""
Given a list of nums with no duplicates in the list, find all the subsets of nums
hello
"""

def find_subsets_no_dups(nums: list[int]) -> list:
    result = []
    current = []
    def subset(i: int) -> None:
        if i == len(nums):
            result.append(current[:])
            return
        current.append(nums[i]) 
        subset(i+1)  
        current.pop()
        subset(i+1)            
        
    subset(0)
    return result
    
"""
Given a list of nums with duplicates in the list all the subsets of nums
"""    
def find_subsets_with_dups(nums: list[int]) -> list:
    result = []
    current = []
    nums.sort()
    def subset(i: int) -> None:
        if i == len(nums):
            result.append(current[:])
            return
        current.append(nums[i]) 
        subset(i+1)  
        current.pop()
        k = 1
        while i+k < len(nums) and nums[i] == nums[i+k]:
            k+=1
        subset(i+k)  
    subset(0)
    return result

# if __name__ == "__main__":
# result = find_subsets_with_dups([6, 6, 2, 3, 3, 4, 4, 5, 5, 5])
"""
[], [2], [3], [2, 2], [2, 3], [3, 3], [3, 2, 3], [2, 3, 3]
"""
# print(len(result))   
# print(result)

[1, 2, 3, 4]

def permutation_with_no_duplicates(nums: list[int]) -> list:
    result = []
    current = []
    def find(visited: set):
        N = len(nums)
        if len(current) == N:
            result.append(current[:])
            return
        for i in range(N):
            if i in visited:
                continue
            current.append(nums[i])
            visited.add(i)
            find(visited)
            current.pop()  
            visited.discard(i)  
    find(visited = set())
    print(result, len(result))
    
permutation_with_no_duplicates(nums=[1, 2, 3, 4])

def permutation_with_duplicates(nums: list[int]) -> list:
    result = []
    current = []
    nums.sort()
    def find(visited: set):
        N = len(nums)
        if len(current) == N:
            result.append(current[:])
            return
        for i in range(N):
            if i in visited:
                continue
            if i > 0 and nums[i] == nums[i-1] and not i-1 in visited:
                continue
            current.append(nums[i])
            visited.add(i)
            find(visited)
            current.pop()  
            visited.discard(i)             
        
    find(visited = set())
    print(result)
    print(len(result))
    
# permutation_with_duplicates([2, 2, 2, 3, 2, 2, 2])

# a = [[1, 2, 3], [1, 3], [1, 2], [2, 3], [1, 3], [2], []]
# a.sort()
# print(a)           
    


