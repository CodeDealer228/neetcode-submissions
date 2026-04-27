class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i,n in enumerate(nums):
            if n not in s:
                s[n] = [i]
            else:
                s[n].append(i)
        for i,n in enumerate(nums):
            need = target-n
            if need in s:
                j_list = s[target-n]
                if i in j_list:
                    j_list_2 = [a for a in j_list if a!=i]
                    if j_list_2:
                        j = j_list_2[0]
                    else:
                        continue
                else:
                    j = j_list[0]         
                return [i, j]
        return -1