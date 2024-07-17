class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs)==1:
            return strs[0]
        sort_str=sorted(strs)
        first=sort_str[0]
        last=sort_str[-1]
        ans=''
        for i in range(min(len(first),len(last))):
            if first[i]!=last[i]:
                return ans
            ans+=first[i]
        return ans 