#### Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

```
Example 1:
Input: hour = 12, minutes = 30
Output: 165
```
```
Example 2:
Input: hour = 3, minutes = 30
Output: 75
```
```
Example 3:
Input: hour = 3, minutes = 15
Output: 7.5
```
```
Example 4:
Input: hour = 4, minutes = 50
Output: 155
```
```
Example 5:
Input: hour = 12, minutes = 0
Output: 0
```

### Constraints:

- 1 <= hour <= 12
- 0 <= minutes <= 59
- Answers within 10^-5 of the actual value will be accepted as correct.  
- The tricky part is determining how the minute hand affects the position of the hour hand.

### Calculate the angles separately then find the difference.

### Code:

### C++:

```
class Solution {
public:
    double angleClock(int hour, int minutes) {
        float k = fabs((30*(hour%12+((float)minutes/60))-minutes*6));
        if(k > 180) k -=360;
        return abs(k);
    }
};
```

### Python:

```
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs(minutes*5.5 - hour*30)
        return min(angle,360-angle)
```
