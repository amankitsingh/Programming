## Program to print pattern 'N' n times in a row;

#Example 1:
```
n=5
c=3

+   + +   + +   +
++  + ++  + ++  +
+ + + + + + + + +
+  ++ +  ++ +  ++
+   + +   + +   +

```

#Example 2:
```
n=6
c=2

+    + +    + 
++   + ++   + 
+ +  + + +  + 
+  + + +  + + 
+   ++ +   ++
+    + +    +

```
#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n,c;
	cout<<"Enter the Size of pattern:";
	cin>>n;
	cout<<"Enter the Number of pattern in a row:";
	cin>>c;
	
	for(int i=0;i<c;i++)
	{
		cout<<"+";
		for(int j=0;j<n-2;j++)
		{
			cout<<" ";
		}
		cout<<"+ ";
	}
	cout<<endl;
	
	for(int k=0;k<n-2;k++)
	{
	    for(int i=0;i<c;i++)
		{
	        cout<<"+";
	        for(int j=0;j<k;j++)
			{
	            cout<<" ";
	        }
	        cout<<"+";
	        for(int j=0;j<n-2-k-1;j++)
			{
	            cout<<" ";
	        }
	        cout<<"+ ";
	    }
	    cout<<endl;	
	}
	
	for(int i=0;i<c;i++)
	{
		cout<<"+";
		for(int j=0;j<n-2;j++)
		{
			cout<<" ";
		}
		cout<<"+ ";
	}
	cout<<endl;
	
	return 0;
}
```
