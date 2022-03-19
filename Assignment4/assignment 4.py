#1. Making a calculator

def readNumber(s,i):
    #list of all values which can be in any number.
    num = [".","0","1","2","3","4","5","6","7","8","9"]
    r = i+1
    n = len(s)
    #pre condition: we put input i from where the number starts.
    #checks whether the value at given r is present in list or not
    #INV: for r <n, s[i:r] is a part of number 
    while r<n:
        # if it is an element of num then we will move to next r
        if s[r] in num:
            r+=1
        # else we will stop 
        else:
            break 
        # post condition: s[i:r] is our required number started from i'th position 
    return (float(s[i:r]),r)

def evalParen(s,i):
    #To get first number using readNumber
    (a,b) = readNumber(s,i+1)
    #if there is only one no. between brackets we will return it as it is
    if s[b] == ')':
        return (a,b+1)
    #To get second number which start after the operator using readNumber 
    (c,d) = readNumber(s,b+1)
    # 4 cases for each possible operation we can do on our numbers represented by 
    # a and c which we gwt using readNumber function
    if s[b] == '+':
        return (a+c,d+1)
    if s[b] == '-':
        return (a-c,d+1)
    if s[b] == '*':
        return (a*c,d+1)
    if s[b] == '/':
        return (a/c,d+1)
    #post condition: we get our evaluated single parenthesized subexpression

def evaluate(s):
    # if there is not any bracket in expression that mean 
    # we can evaluate it easily using evalParen 
    if "(" not in s: 
        (c,d) = evalParen("("+s+")",0)
        return c
    l = 0
    start = 0 
    #pre condition: we have our non evaluated string expression s 
    while l < len(s):
        # INV : for 0<= start <= l < len(s) we have start equal to the index of innermost parenthesis 
        if s[l] == "(":
            start = l
        l+=1
        # here we break loop if we find ) which means 
        # it is the end of our single parenthesized subexpression
        if s[l] == ")":
            break
    # here we will evaluate our subexpression using evalParen
    (a,b) = evalParen(s,start)
    # finally we will change our evaluated answer to string and 
    # add it again to the original string by removing brackets
    # and put new string again in evaluate to calculate the new expression. 
    return evaluate(s[0:start]+str(a)+s[b:len(s)])

#####################################################################
#2. A sequence of unique sums

def sumSequence(n):
    # list for n=1
    if n == 1: 
        return [1]
    # list for n =2 
    if n == 2:
        return [1,2]
    b = [1,2]
    c = 3
    i = 3
    # precondition: we have list for n = 2 as b=[1,2]  
    #INV3: 2<i<=n and we have list b = [1,2,...Ai]
    while i<=n:
        count = 0 
        l = 0
        #INV2: 0<=l<len(b) and count is total no. of pairs whose sum is c present in b[l:n].
        # and we will end loop if count gets greater than 1
        while l < len(b):
            # b[l] < c//2 as b[r]>b[l] and 
            # if b[l]>c//2  then b[l]+b[r]>c which is wrong
            if b[l] > c//2:
                break
            #we will start r from l+1 so that elements don't repeat
            r = l+1
            #INV1: l<r<len(b) , b[l]+b[r]<=c 
            # and count will increase by 1 if for any r, b[l]+b[r] = c
            while r < len(b):
                #b[l]+b[r]<=c always 
                if b[l]+b[r] < c:
                    r+=1
                # we will add 1 in count as we get a pair whose sum is c
                elif b[l]+b[r] == c:
                    count+=1
                    r+=1
                #if sum exceeds c then we will break the loop as remaining pairs will be greater then c
                elif b[l]+b[r] > c:
                    break
                #postcondition1: we get count += 1 if there is any r for which b[l]+b[r] = c
            # if count>1 means we get more than one pairs so we will move to next c 
            if count > 1:
                break
            l+=1
            #postcondition2: we get either count = 1 if there is only one pair in list b 
            # else loop will break and we will move to next c.  
        #if count = 1 mean we get exactly one pair so c is the next term in our sequence
        if count == 1:
            #we will append c to list and move to next i till i = n. 
            b.append(c)
            i+=1
        c+=1
    # post condition3: we will return list b = [1,2,3,...,An]        
    return b 

#################################################################################################
#3. Shortest sublist with suficient sum

def minLength(a,x):
    # precondition: we have taken initially min as n+1 
    n = len(a)
    min = n+1
    # INV2 : min is the minimum length of all sublists starting from index < left 
    for left in range (0,n):
        # start the sum with with a[left] as initial sum 
        sum = a[left]
        # if the first term itself is greater than x 
        if sum > x:
            return 1
        else:
            #INV1 : for left < right < n, min is the minimum length of
            # sublist of a[left:right] whose sum is greater than x
            for right in range (left+1,n):
                #to add next term in the existing sum 
                sum+=a[right]
                # here if sum > x and also length of sublist < min we will update min 
                if sum > x and right - left + 1  < min:
                    min = right-left + 1
                    break
                #postcondition1: we will get min length of sublist of a[left:n] whose sum is greater than x
        #postcondition2: we will get final min length of sublist of a whose sum is greater than x 
    # if min = n+1 which means we don't get any sublist with sum > x 
    # so we will return -1
    if min == n+1:
        return -1
    else:
        return min

###############################################################################
#4. Merging an contact list 

#	Merges two subarrays of	a[]	write the output to	a[l:r] 
#	First subarray is a[l:m] # Second subarray is a[m:r]	
def mergeab(a,b,l,m,r):
    i = l
    j = m 
    k = l
    while i < m and j < r:
        if a[i] < a[j]:
            b[k] = a[i]
            i = i+1
        else:
            b[k] = a[j]
            j = j+1
        k = k+1
    # Copy the remaining elements of a[i:m], if there are any
    while i < m:
        b[k]=a[i]
        i = i+1
        k = k+1
    # Copy the remaining elements of a[j:r], if	there are any	
    while j < r:
        b[k]=a[j]
        j = j+1
        k = k+1
    # copy all elements of b to a again and give list a as sorted
    for i in range(l,r):
        a[i] = b[i]
    return a

#used to return a sorted list from a given input list a
def mergesort(a):
    n = len(a)
    # making a array to copy sorted list
    b = [0]*n
    # initialising block with length 1
    block = 1
    # at each step consecutive 'block' number of elements are sorted
    while(block<n):
        for i in range(0,n,2*block):
            if i+block > n:
                mergeab(a,b,i,n,n)
            elif i+2*block > n:
                mergeab(a,b,i,i+block,n)
            else:
                mergeab(a,b,i,i+block,i+2*block)
        # increasing block 2 times 
        block*=2
    # in the end by increasing blocks we will get our whole list sorted
    return a

def mergeContacts(a):
    # using sorted list
    l = mergesort(a)
    i=0
    k=0
    # making a array to copy elements
    b = [("0",["0"])]*len(a)
    #INV : b = (merged list till i'th element)+[("0"),["0"]]*(n-i)
    while i < len(a):
        (c,d) = l[i-1]
        (e,f) = l[i]
        (g,h) = b[k-1]
        #if initials of i'th element is not equal to previous element then 
        # we can increase k and copy it as separate element
        if c != e:
            b[k] = (e,[f])
            k = k+1
        # if initials of i'th element is equal to previous element then
        # we will take email from i'th element and add it with the (k-1)th element's email ID 
        # we will also remove 1 element from b as we are not using it's one element
        else:
            b[k-1] = (g,h+[f])
            b.pop()
        i+=1
    #post condition: we will get b as final list with all merged email's with common initials
    return b
#%%


# %%
