<h2>  Third Maximum Number</h2><hr><div><p>Given an integer array <code>nums</code>, return <em>the <strong>third distinct maximum</strong> number in this array. If the third maximum does not exist, return the <strong>maximum</strong> number</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [3,2,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [2,2,3,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Can you find an <code>O(n)</code> solution?</div>


Answer 1
```
from sortedcontainers import SortedSet

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_array = SortedSet()
        for x in nums:
            if x in max_array:
                continue
            if len(max_array) == 3:
                max_array.add(x)
                max_array.discard(max_array[0])
            else:
                max_array.add(x)
        
        if len(max_array) == 3:
            return max_array[0]
        else:
            return max_array[-1]
```            
Answer 2

```
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        firmax = -inf
        secmax = -inf
        thrmax = -inf
        
        for x in nums:
            if x == firmax or x == secmax or x == thrmax:
                continue
                
            if x > firmax:
                thrmax,secmax = secmax,thrmax
                secmax,firmax = firmax,x
            elif x > secmax:
                thrmax,secmax = secmax,x
            elif x > thrmax:
                thrmax = x
        
        if thrmax == -inf:
            return firmax
        return thrmax
```
