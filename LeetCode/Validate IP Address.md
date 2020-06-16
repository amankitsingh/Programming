## Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

### IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

### Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

### IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

### However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

### Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

- Note: You may assume there is no extra space or special characters in the input string.
```
Example 1:
Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".
```
```
Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".
```
```
Example 3:
Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.
```

`
- There are many ways to do this quesiton:

---

### Code:

## 1 way:

```
import re
class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP.count(".") == 3:
            if IP[-1] == ".":
                return "Neither"
            else:
                ips = IP.split(".")
                for x in ips:
                    if (len(x) == 0 or len(x) > 3) or (not x.isdigit() or int(x)>255):
                        return "Neither"
                    if(x[0] == "0" and len(x) != 1):
                        return "Neither"
                    for i in x:
                        if not i.isdigit():
                            return "Neither"
            return "IPv4"
        elif IP.count(":") == 7:
            if IP[-1] == ":":
                return "Neither"
            else:
                ips = IP.split(":")
                for x in ips:
                    if (len(x) == 0 or len(x) > 4):
                        return "Neither"
                    for i in x:
                        if (not (i>='0' and i<='9' or i>='a' and i<='f' or i>='A' and i<='F')):
                            return "Neither"
            return "IPv6"
        else:
            return "Neither"
```

## 2 way:

```
from ipaddress import ip_address, IPv6Address
class Solution:
    def validIPAddress(self, IP: str) -> str:
        try:
            return "IPv6" if type(ip_address(IP)) is IPv6Address else "IPv4"
        except ValueError:
            return "Neither"
```

## 3 way:

```
import re
class Solution:
    chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    patten_IPv4 = re.compile(r'^(' + chunk_IPv4 + r'\.){3}' + chunk_IPv4 + r'$')
    
    chunk_IPv6 = r'([0-9a-fA-F]{1,4})'
    patten_IPv6 = re.compile(r'^(' + chunk_IPv6 + r'\:){7}' + chunk_IPv6 + r'$')

    def validIPAddress(self, IP: str) -> str:        
        if self.patten_IPv4.match(IP):
            return "IPv4"
        return "IPv6" if self.patten_IPv6.match(IP) else "Neither" 
```

## 4 way:

- Divide and Conquer

### Algorithm

```
For the IPv4 address, we split IP into four chunks by the delimiter ., while for IPv6 address, we split IP into eight chunks by the delimiter :.

For each substring of "IPv4" address, we check if it is an integer between 0 - 255, and there is no leading zeros.

For each substring of "IPv6" address, we check if it's a hexadecimal number of length 1 - 4.
```

```
class Solution:
    def validate_IPv4(self, IP: str) -> str:
        nums = IP.split('.')
        for x in nums:
            # Validate integer in range (0, 255):
            # 1. length of chunk is between 1 and 3
            if len(x) == 0 or len(x) > 3:
                return "Neither"
            # 2. no extra leading zeros
            # 3. only digits are allowed
            # 4. less than 255
            if x[0] == '0' and len(x) != 1 or not x.isdigit() or int(x) > 255:
                return "Neither"
        return "IPv4"
    
    def validate_IPv6(self, IP: str) -> str:
        nums = IP.split(':')
        hexdigits = '0123456789abcdefABCDEF'
        for x in nums:
            # Validate hexadecimal in range (0, 2**16):
            # 1. at least one and not more than 4 hexdigits in one chunk
            # 2. only hexdigits are allowed: 0-9, a-f, A-F
            if len(x) == 0 or len(x) > 4 or not all(c in hexdigits for c in x):
                return "Neither"
        return "IPv6"
        
    def validIPAddress(self, IP: str) -> str:
        if IP.count('.') == 3:
            return self.validate_IPv4(IP)
        elif IP.count(':') == 7:
            return self.validate_IPv6(IP)
        else:
            return "Neither"
```
