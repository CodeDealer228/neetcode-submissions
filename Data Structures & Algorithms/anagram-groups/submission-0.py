class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = [(''.join(sorted(w)),i) for i,w in enumerate(strs)]
        words.sort()
        answer = []
        last_sorted_str = None
        for sorted_w,i in words:
            if last_sorted_str != sorted_w:
                answer.append([])
            answer[-1].append(strs[i])
            last_sorted_str = sorted_w
        return answer

        