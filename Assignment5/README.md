# Introduction
This is one of the assignment of my course COL100. In this I have made code for three problems which are:
* 1. Play with Grid
* 2. String Problem
* 3. Calendar Maker

## Play with Grid
This is a board game in which players are given a *MxN* grid *G* with non-negative penalty values at each point *G(i; j)*.</br>
player begin at the upper left corner (0; 0) and must reach at the opposite corner *(M - 1;N - 1)* to complete this game.</br>
At each step, a player can go one step in the direction of the target, either vertically, horizontally, or diagonally (i.e., from cell *i,j*), we can only go to cells (*i+1; j*), (*i, j +1*), or (*i+1; j +1*).
Every time we step into a cell, we shall incur the penalty of that cell.</br>
As a result, we can use this code to determine a route with the least total penalty. (The total penalty is the sum of all fines).

## String Problem
Given two lower case letter strings A and B, and if A can be transformed to B with the fewest number of adjustments as follows:
* Insert a character in A.
* Delete a character from A.
* Replace a character in A subject to restriction: 
  * a vowel can be replaced with only a vowel
  * a consonant may be replaced with either vowel or consonant.
  
The final output must be the minimal number of adjustments that will turn A into B, even if there are numerous answers to the same inputs.</br>
For example : Let Input:A= "bplpcd" and B= "apple" then one output can be 5 but the minimum answer will be 4.

## Calendar Maker 
This code can be used to print a calendar to a text file in a formatted manner for a given year.
The calendar prints all 12 months and days of the week on a single page in a neat fashion that can be printed for usage.
It correctly computes the day for January 1<sup>st</sup>.
It's assumed that the function's input is more than 1753 due to the fact that the calendar changed from the Julian calendar to the Gregorian calendar in 1752.

The Output for our function will be as follows: 

![a](Assignment5/Calendar-2022.png)
