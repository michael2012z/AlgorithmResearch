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
Given a rod of length n inches and a table of prices p~i~ for i = 1, 2, ..., n, determine the maximum revenue r~n~ obtainable by cutting up the rod and selling the pieces. Note that if the price p~n~ for a rod of length n is large enough, an optimal solution may require no cutting at all.

### Matrix-chain multiplication

### Longest common subsequence
