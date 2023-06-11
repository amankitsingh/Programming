<h2>  Squares of a Sorted Array</h2><hr><div><p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing</strong> order, return <em>an array of <strong>the squares of each number</strong> sorted in non-decreasing order</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [-4,-1,0,3,10]
<strong>Output:</strong> [0,1,9,16,100]
<strong>Explanation:</strong> After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [-7,-3,2,3,11]
<strong>Output:</strong> [4,9,9,49,121]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code><span>1 &lt;= nums.length &lt;= </span>10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Squaring each element and sorting the new array is very trivial, could you find an <code>O(n)</code> solution using a different approach?</div>

Answer1
```
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            nums[i] = pow(nums[i],2)
            
        return sorted(nums)
```
Answer2
```
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r,n = 0, len(nums)-1, len(nums)
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i]*=-1
                
        result = [0] * n
        n-=1
        while n >= 0:
            if nums[l] > nums[r]:
                result[n] = nums[l]
                l+=1
            else:
                result[n] = nums[r]
                r-=1
            n-=1
        
        for i in range(len(result)):
            result[i]*=result[i]
        return result
```
