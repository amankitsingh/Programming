<h2>  Move Zeroes</h2><hr><div><p>Given an integer array <code>nums</code>, move all <code>0</code>'s to the end of it while maintaining the relative order of the non-zero elements.</p>

<p><strong>Note</strong> that you must do this in-place without making a copy of the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [0,1,0,3,12]
<strong>Output:</strong> [1,3,12,0,0]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you minimize the total number of operations done?</div>


Answer 

```
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums)<2:
            return
        i,j= 0,1
        while j < len(nums):
            if nums[i] == 0 and nums[j] != 0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
            elif nums[i] != 0 and nums[j] == 0:
                i = j
                j+=1
            else:
                j+=1
```
