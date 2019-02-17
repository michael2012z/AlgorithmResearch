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
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|S|b|c|a|b|c|a|b|c|a|b|d|a|a|a|d|d|
|P|||a|b|c|a|b|d|
|||||||||^|

Then the algorithm continue to compare P against S at index 3, like:

|Index|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
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
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|S|b|c|a|b|c|a|b|c|a|b|d|a|a|a|d|d|
|P|||a|b|c|a|b|d|
|||||||||^|

When we find S[7] doesn't match P[5], it is inefficient to come back to S[3] to compare again. Because we have known that a matching string can't be found at S[3] or S[4] because even the starting character is different.

But starting from S[5] is a good idea, because the first 2 characters are same with P.

KMP algorithm aims to improve the efficiency in this way: make the roll-back steps as less as possible. To achieve this, pre-processing the pattern string P is required.

In the begining of the algorithm, KMP algorithm handle the pattern string P to build a table, the table **T** is of the same size of P. Each item of T specifies the roll-back steps when a mis-matching is found at current position (in P).

In the case above, the roll-back steps at P[5] ("d") should be 2. In next step, the algorithm should move back 2 characters, in S rather than P, to S[5] to continue the compare.

|Index|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|S|b|c|a|b|c|a|b|c|a|b|d|a|a|a|d|d|
|P||||||a|b|c|a|b|d|
|||||||^|

#### Computing T

The key of KMP algorithm is to compute the table T.

The idea how KMP boost the string scaning is: If the leading sub-string of the pattern didn't appear inside the pattern string, when a mismatch was found, we can continue to compare next character in **S**; otherwise we fall back by some steps.

The algorithm is described in human language as:
- For a location in P that's NOT repeating the leading part (any length of chars) of the pattern string, the corresponding location in **T** should be "0" as no fall-back should be made.
- For a location in P that's repeating the leading part, the corresponding location in **T** should be non-zero, means some fall-back is needed. The steps to fall back depends on how far current repeating sub-string has matched with the leading part of P. The reason is: when the leading sub-string appears inside P, we need to check if a matching appear there.

In our case, **T** of the pattern **T** would looks like:

|Index|0|1|2|3|4|5|
|-|-|-|-|-|-|-|
|P|a|b|c|a|b|d|
|T|-1|0|0|0|1|2|
||||^||^|

Let me explain how the scanning works by examples:
1. When you comes to P[2] ("c") and finds a mismatch between S and P, you can simply restart the matching from next position of P, because in the characters you have covered so far in current matching (with "abc"), "a" or "ab" haven't appeared again, and you don't need to worry some matching was missing. So it is 0 step that you need to roll back.
2. If a mismatch happened in P[4] ("b"). You have to worry more. Because P[3]~P[4] ("ab") is repeating the leading part of the pattern string. You need to begin next examing to see if a matching starts from P[3]. So now you need to rool back 1 step to compare if P and S matches at there, as they both have "a" at that location.

Is the algorithm mentioned above good? Yes. But is it good enough? No. It can be further optimized.

Let's look into case 2 of the example above. When you are at P[4] ("b") and found a mismatch, you are in a repeating leading sub-string ("ab" in P[3,4] repeats "ab" in P[0,1]). If current chararacter in S doesn't match "b", if won't match even if you roll back 1 step and restart the comparasion there, because the examing must fail again at the same "b" in S.

So the 2nd rule can be further optimized as:
- For a location in P that's repeating the leading part, the corresponding location in **T** should be "0", too. When the repeating end, the T value for the comming non-repeating character should be "how far current repeating sub-string has matched".

The **T** values should be:

|Index|0|1|2|3|4|5|
|-|-|-|-|-|-|-|
|P|a|b|c|a|b|d|
|T|-1|0|0|-1|0|2|

Where is "-1" in T comes from? The first "-1" is the special handling for the leading member, means "when the first char mismatches, move to next (roll-back -1 step)". And "-1" can repeat in T whenever the leading char appears.

In the implementation of T. When the leading sub-string is repeating in P, we just simply copy the T values of leading sub-string. And set the matching length of the leading-substring to the comming mis-matched location.

#### Example

Shown above.

#### Efficiency
O(n)

