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
