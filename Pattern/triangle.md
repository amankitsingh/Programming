### To make the pattern something like this.

### 1:

```
n = 3
  1
 *2*
**3**
 *2*
  1
```

### 2:

```
n = 5
     1
    *2*
   **3**
  ***4***
 ****5****
  ***4***
   **3**
    *2*
     1
```

### 3:

```
 n = 10
          1
         *2*
        **3**
       ***4***
      ****5****
     *****6*****
    ******7******
   *******8*******
  ********9********
 *********10********
  ********9********
   *******8*******
    ******7******
     *****6*****
      ****5****
       ***4***
        **3**
         *2*
          1
```

### Code:

```
#include<bits/stdc++.h>
using namespace std;
int main(){
	int n;
	cin>>n;
	
	for(int i=1;i<=n;++i){
		for(int j=n-i;j>0;--j)
			cout<<" ";
		
		if(i>1)
			for(int k=i-1;k>0;--k)
				cout<<"*";
		
		cout<<i;
		
		if(i>1)
			for(int k=i-1;k>0;--k)
				cout<<"*";
		for(int j=n-i;j>0;--j)
			cout<<" ";
		cout<<endl;
	}
	
	for(int i=1;i<n;++i){
		for(int j=i;j>0;--j)
			cout<<" ";
		
		if(i>=1)
			for(int k=n-1-i;k>0;--k)
				cout<<"*";
		
		cout<<n-i;
		
		if(i>=1)
			for(int k=n-1-i;k>0;--k)
				cout<<"*";
		for(int j=i;j>0;--j)
			cout<<" ";
		cout<<endl;
	}
	return 0;
}
```
