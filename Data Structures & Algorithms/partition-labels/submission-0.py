class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_index = {}

        for i in range(len(s)):
            last_index[s[i]] = i
        
        cur_length = 0
        cur_last_index = 0
        res = []
        for i in range(len(s)):
            cur_last_index = max(cur_last_index, last_index[s[i]])

            if i == cur_last_index:
                res.append(cur_length+1)
                cur_length = 0
                cur_last_index = 0
            else:
                cur_length += 1
        
        return res
