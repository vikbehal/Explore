### Dynamic Connectivity Problem can be solved using:

#### 1. [Quick Find](http://researchhubs.com/post/computing/algorithm-1/quick-find.html). This is an eager algorithm  
- DS: Array
- Complexity: Union is an expensive operation. Complexity is of order n^2 for n union commands on n objects  

#### Quick Union. This is a lazy approach  
- We try to avoid doing work, until we have to  
- DS: Array
- Complexity: find operation could be of complexity n  

Quick-find issue:  
- Union too expensive (n array accesses)  
- Trees are flat, but too expensive to keep them flat  

Quick-union:  
- Trees can get tall  
- Find too expensive (could be n array accesses) if tree if skewed in one direction 

