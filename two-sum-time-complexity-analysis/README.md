# Time Complexity Analysis of Two Sum
**Author:** John Hill 
 **Date:** October 25th, 2021

### Prompt:
In this part, your job is to write a short report comparing each of the algorithms using the data collected from Part 2. Your report should include the following for each algorithm:

1. Graphs of the runtime of your experiments as a function of n
2. A description of the algorithm’s asymptotic runtime complexity (what is its Big Oh?) and whether the graph supports your asymptotic analysis
3. Finally, your report should conclude with a discussion of which algorithm is better to use in practice. Are there situations where the highest performing algorithm would be inferior to one of the other algorithms? Why or why not?
### Graphs: 
![Brute Force](BruteForce.png)
**Figure 1:** *Brute Force run time* 

![Binary Search](BinarySearch.png)
**Figure 2:** *Binary Search run time* 
![Hash Set](HashSet.png)
**Figure 3:** *Hash Set run time* 
![Sorting and Sweeping](SortAndSweeping.png)
**Figure 4:** *Sorting and Sweeping run time*
![All but Brute Force](AllButBrute.png) 
**Figure 5:** *All solutions but Brute Force*

### Asymptotic Runtime Complexity Analysis:
* **Brute Force:**
    * O($n^2$)
        * Because we are treversing the arrays twice, this does match up with data shown in graphs 
* **Binary Search:**
    * O(log n + n log n) = O(n log n), outside of a few edgecases the returned run times do seem to match up with what a n log n run time would look like
* **Hashset:**
    * O(n) assuming both sets are equal length, matches up very well as runtime does not appear to be increasing much at all 
* **Sorting and Sweeping:**
    * O(n log n), similar to binary search outside of a few edge cases the data supports the n log n time complexity
### Conclusion:
I think that hashset would be the most practical for real world use, with a time complexity of O(n), I think that the other solutions such as sorting and sweeping are extremely fast but just do not match the speed of a hash set. I the only way I could see an issue with hashing is if you are more concerned with space complexity as opposed to speed becasue we need to create the dictionary which can be expensive regarding space. 