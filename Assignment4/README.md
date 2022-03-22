# Introduction
This is one of the assignment of my course COL100. In this I have made code for four problems which are:
* 1. Calculator
* 2. Ulam Number Sequence
* 3. Shortest sublist with sufficient sum
* 4. Contact list Merger

## Calculator
This is a function that evaluates a string representation of a simple mathematical statement, such as "(1+2)\*3," to produce the resultant number.
The input string may include any of the following: positive numbers, +, -, \*, /, (, ). </br>
The numbers may or may not contain a decimal part, e.g. the number 3 could be given as "3" or as "3.0" or with any number of zeroes. All expressions will be fully parenthesized, e.g. there will only be given "(1+(2\*3))-4", not "1+2\*3-4".

## Ulam Number Sequence
This is a function to generate the Ulam number sequence. </br>
Ulam number sequence can be given by: </br>
<p align="center">
   1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, ... 
</p>
This is how the sequence is put together. 1 and 2 are the first and second elements, respectively. The next number is the smallest positive number bigger than the previous one that is equal to the sum of two distinct integers (that are already in the series) in exactly one way. </br>
Because there are only two numbers in the starting sequence, the next number after 1 and 2 is 3 = 1 + 2. </br>
After 3, the following number is 4 = 3 + 1. Although 4 = 2 + 2 is valid, this equation does not count since the two addends must be distinct. </br>
The next number cannot be 5, because 5 = 1 + 4 but also 5 = 2 + 3: there should only be one way to produce a number in the series by adding two separate integers. 6(2 + 4) is the next number. </br>
7 can be made in two ways (1 + 6 or 3 + 4), hence the next number is 8 (2 + 6). And so forth.

## Shortest sublist with sufficient sum
In this problem, we have made a function to select as few elements from a given list of numbers as feasible so that their sum strictly surpasses a specific amount *n*.
The numbers must, however, be sequential to constitute a contiguous sublist. So, if the list is A = [9,-4,7,5,2,-3,8] and we want a sum greater than 15, we can't just take the 9 and the 8. We need to choose a continuous sublist of numbers, and [9,-4,7,5] is the shortest one with a large enough sum.

## Contact list Merger
This is a function used to merge a contact list in a specific manner.
Suppose, we have a contact list as a list of name & email address pairs, for example:
<p align="center">
[("TST","tanish@gmail.com"), ("ES","ekansh@gmail.com"), ("TST","Tanish.singh@yahoo.com")]
</p>
We have to clean this up to gather all the email addresses of each person together. This will
result in a list of pairs where the first component is the name and the second component is a
list of email addresses, for example:
<p align="center">
[("ES",["ekansh@gmail.com"]), ("TST",["tanish@gmail.com","Tanish.singh@yahoo.com"])]
</p>
