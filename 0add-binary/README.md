<h2>  Add Binary</h2><hr><div><p>Given two binary strings <code>a</code> and <code>b</code>, return <em>their sum as a binary string</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> a = "11", b = "1"
<strong>Output:</strong> "100"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> a = "1010", b = "1011"
<strong>Output:</strong> "10101"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= a.length, b.length &lt;= 10<sup>4</sup></code></li>
	<li><code>a</code> and <code>b</code> consist&nbsp;only of <code>'0'</code> or <code>'1'</code> characters.</li>
	<li>Each string does not contain leading zeros except for the zero itself.</li>
</ul>
</div>

Answer
```
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i,j,carry,result = len(a)-1,len(b)-1, 0, ""
        while i>=0 or j>=0:
            sump = carry
            if i >=0: sump += ord(a[i]) - ord('0')
            if j >=0: sump += ord(b[j]) - ord('0')
            i,j = i-1,j-1
            result += str(sump%2)
            carry = 1 if sump > 1 else 0
        if carry: result+=str(carry)
        return result[::-1]
```
