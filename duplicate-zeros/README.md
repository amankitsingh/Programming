<h2>  Duplicate Zeros</h2><hr><div><p>Given a fixed-length integer array <code>arr</code>, duplicate each occurrence of zero, shifting the remaining elements to the right.</p>

<p><strong>Note</strong> that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> arr = [1,0,2,3,0,4,5,0]
<strong>Output:</strong> [1,0,0,2,3,0,0,4]
<strong>Explanation:</strong> After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> arr = [1,2,3]
<strong>Output:</strong> [1,2,3]
<strong>Explanation:</strong> After calling your function, the input array is modified to: [1,2,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;= 9</code></li>
</ul>
</div>

Answer1:
<code>
	class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i<len(arr)-1:
            if arr[i] == 0:
                last_index=0
                for x in range(len(arr)-1,i, -1):
                    arr[x] = arr[x-1]
                    last_index = x
                arr[last_index] = 0
                i=last_index+1
            else:
                i+=1
        return arr
                
        
</code>
	
Answer2:
	
<code>
	j=0
        i=0
        while i <len(arr):
           
            if arr[i]==0:
                
                arr.insert(i,0)
                i+=2
                arr.pop()
            else:
                i+=1
</code>
