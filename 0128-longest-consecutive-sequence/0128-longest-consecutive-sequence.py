class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        st = set()
        for i in range(n):
            st.add(nums[i])
        largest =1
        for i in st:
            if i-1 not in st:
                cnt=1
                x=i
                while x+1 in st:
                    cnt+=1
                    x+=1
                largest = max(largest,cnt)
        return largest