## Strings: Making Anagrams
```
Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?

Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character deletions required to make  a and b anagrams. Any characters can be deleted from either of the strings.

For example, if a=cde and b=dcf, we can delete e from string a and f from string b so that both remaining strings are cd and dc which are anagrams.
```
### Sample Input

```
cde
abc
```

### Sample Output

```
4
```

### Code:

```
#include <bits/stdc++.h>

using namespace std;

// Complete the makeAnagram function below.
int makeAnagram(string a, string b) {
    auto count = 0;
    vector<int> freq(26, 0);
    for (auto c : a) { ++freq[c - 'a']; }
    for (auto c : b) { --freq[c - 'a']; }
    for (auto val : freq) { count += abs(val); }
    return count;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string a;
    getline(cin, a);

    string b;
    getline(cin, b);

    int res = makeAnagram(a, b);

    fout << res << "\n";

    fout.close();

    return 0;
}
```
