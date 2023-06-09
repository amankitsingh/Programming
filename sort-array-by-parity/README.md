<h2>  Sort Array By Parity</h2><hr><div><p>Given an integer array <code>nums</code>, move all the even integers at the beginning of the array followed by all the odd integers.</p>

<p>Return <em><strong>any array</strong> that satisfies this condition</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [3,1,2,4]
<strong>Output:</strong> [2,4,3,1]
<strong>Explanation:</strong> The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 5000</code></li>
</ul>
</div>

Answer1
```
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i,x=0,0
        while i < len(nums)-1:
            if nums[x]%2 != 0:
                nums.append(nums[x])
                del nums[x]
            else:
                x+=1
            i+=1
        return nums
```

Answer2

```
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i,j=0,len(nums)-1
        while i<j:
            if nums[i]%2>nums[j]%2:
                nums[i],nums[j] = nums[j],nums[i]
            
            if nums[i]%2==0: i+=1
            if nums[j]%2==1: j-=1
        return nums
```
