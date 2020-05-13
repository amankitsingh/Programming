## You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.
```
Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
```
```
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
```

# Note: Your solution should run in O(log n) time and O(1) space.

Check if the next number is same or not, for each 2 number

```
int singleNonDuplicate(vector<int>& nums) {
	    for (int i = 0; i < nums.size()-1; i+= 2)
        {
            if (nums[i] != nums[i+1])
            {
                return nums[i];
            }
        }
    
    return nums.back();
```
