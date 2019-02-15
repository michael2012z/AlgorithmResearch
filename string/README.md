# String Searching Algorithms

## Question setting
Given the string to be searched as **S**, the pattern string as **P**. The algorithm need to determine if S contains P, and specify the location(s) inside S.
Example:
S = "bcabcabcabdaaadd"
P = "abcabd"
S contains P at index 5 (0 based): "bcabc**abcabd**aaadd".
The algorithm should return a list containing "5", like (in python):
 ~ [5]
 
---
## Brute Force Algorithm
#### Idea
The idea of brute force algorithm is naive.
From the begining of S, begin to compare each character in S and P:
- if every characters match till the end of P, a location found,
- other wise, failed to find a match in current location of S, move to next character and compare again.

#### Example

When the algorithm proceed to current location, S[7] was found mismatching P[5].

|Index|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|
|-|-|
|S|b|c|a|b|c|a|b|c|a|b|d|a|a|a|d|d|
|P|||a|b|c|a|b|d|
|||||||||^|

Then the algorithm continue to compare P against S at index 3, like:

|Index|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|
|-|-|
|S|b|c|a|b|c|a|b|c|a|b|d|a|a|a|d|d|
|P||||a|b|c|a|b|d|
|||||^|

#### Efficiency
O(n^2^)

---
## Knuth–Morris–Pratt (KMP) Algorithm

#### Idea
Come back to following position:

|Index|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|
|-|-|
|S|b|c|a|b|c|a|b|c|a|b|d|a|a|a|d|d|
|P|||a|b|c|a|b|d|
|||||||||^|

When we find S[7] doesn't match P[5], it is inefficient to come back to S[3] to compare again. Because we have known that a matching string can't be found at S[3] or S[4] because even the starting character is different.

But starting from S[5] is a good idea, because the first 2 characters are same with P.

KMP algorithm aims to improve the efficiency in this way: make the roll-back steps as less as possible. To achieve this, pre-processing the pattern string P is required.

In the begining of the algorithm, KMP algorithm handle the pattern string P to build a table, the table **T** is of the same size of P. Each item of T specifies the roll-back steps when a mis-matching is found at current position (in P).

In the case above, the roll-back steps at P[5] ("d") should be 2. In next step, the algorithm should move back 2 characters, in S rather than P, to S[5] to continue the compare.

|Index|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|
|-|-|
|S|b|c|a|b|c|a|b|c|a|b|d|a|a|a|d|d|
|P||||||a|b|c|a|b|d|
|||||||^|

#### Computing T

The key of KMP optimizition is to compute the table T.

#### Example

#### Efficiency


