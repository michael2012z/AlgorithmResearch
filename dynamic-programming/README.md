# Dynamic Programming
Dynamic programming applies when the subproblems overlapthat is, when subproblems share subsubproblems. 
A dynamic-programming algorithm solves each subsubproblem just once and then saves its answer in a table, thereby avoiding the work of recomputing the answer every time it solves each subsubproblem.

## Steps
When developing a dynamic-programming algorithm, we follow a sequence of
four steps:
1. Characterize the structure of an optimal solution.
2. Recursively define the value of an optimal solution.
3. Compute the value of an optimal solution, typically in a bottom-up fashion.
4. Construct an optimal solution from computed information.

## Cases

### Rod cutting

#### Problem description
Given a rod of length n inches and a table of prices p<sub>i</sub> for i = 1, 2, ..., n, determine the maximum revenue r<sub>n</sub> obtainable by cutting up the rod and selling the pieces. Note that if the price p<sub>n</sub> for a rod of length n is large enough, an optimal solution may require no cutting at all.

#### Optimal substructure
The problem can be broken down into sub-problems:
r<sub>n</sub> = max (r<sub>1</sub> + r<sub>n-1</sub>, r<sub>2</sub> + r<sub>n-2</sub>, ..., r<sub>n-1</sub> + r<sub>1</sub>, p<sub>n</sub>)

#### Implementation
##### Recursive top-down implementation
https://github.com/michael2012z/algorithms/blob/master/dynamic-programming/rod-cutting.py#L2

##### Memoized top-down implementation
The raw recursive top-down implementation can be optimized by recording the result of sub-problems during the recursion.
https://github.com/michael2012z/algorithms/blob/master/dynamic-programming/rod-cutting.py#L16

##### Bottom-up implementation
Bottom-up implementation starts from the most elementary sub-problems and build result of higher level problem from existing results.
https://github.com/michael2012z/algorithms/blob/master/dynamic-programming/rod-cutting.py#L37

##### Solution
A solution was made in bottom-up implementation.
https://github.com/michael2012z/algorithms/blob/master/dynamic-programming/rod-cutting.py#L52
The solution is possible in top-down implementation as well.

### Matrix-chain multiplication

#### Problem description
Given a chain <A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>n</sub>> of n matrices, where for i D 1, 2, ..., n, matrix A<sub>i</sub> has dimension p<sub>i-1</sub> x p<sub>i</sub>, fully parenthesize the product A<sub>1</sub>A<sub>2</sub>...A<sub>n</sub> in a way that minimizes the number of scalar multiplications.

#### Optimal substructure
Let m<sub>i,j</sub> be the minimum number of scalar multiplications needed to compute the matrix Am<sub>i..j</sub> ; for the full problem, the lowestcost way to compute A<sub>1..n</sub> would thus be m<sub>1..n</sub>.
m<sub>i,j</sub> = 
- min( m<sub>i,j</sub> 


### Longest common subsequence
#### Problem description
The meaning of longest common subsequence is straight forward. Let's see an example. Let X = "ABCBDAB" and Y = "BDCABA", the longest common subsequence (LCS) is "BCBA", the length is 4.

#### Optimal substructure
Let i the index of string X, j the index of string Y, l(i, j) the length of longest common subsequence of \[x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>i</sub>\] and \[y<sub>1</sub>, y<sub>2</sub>, ..., y<sub>j</sub>\]. i and j are 0-based. We have recursive optimal solution:

l(i, j) = 
- 0, if i=0 or j=0;
- l(i-1, j-1), if i, j > 0 and x<sub>i</sub>=y<sub>j</sub>;
- max(l(i-1, j), l(i, j-1)), if i, j > 0 and x<sub>i</sub>!=y<sub>j</sub>;

#### Implementation
##### Recursive top-down implementation
The raw recursive solution of the optimal substructure. See https://github.com/michael2012z/algorithms/blob/master/dynamic-programming/longest-common-subsequence.py#L2

##### Bottom-up implementation

|i\j (0\0)|0|1 (B)|2 (D)|3 (C)|4 (A)|5 (B)|6 (A)|
|-|-|-|-|-|-|-|-|
|0 |0|0|0|0|0|0|0|
|1 (A)|0|0|0|0|1|1|1|
|2 (B)|0|1|1|1|1|2|2|
|3 (C)|0|1|1|2|2|2|2|
|4 (B)|0|1|1|2|2|3|3|
|5 (D)|0|1|2|2|2|3|2|
|6 (A)|0|1|2|2|3|3|4|
|7 (B)|0|1|2|2|3|4|4|
