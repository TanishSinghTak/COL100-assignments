#1. Play with Grid

def gridPlay(G):
    m = len(G) 
    n = len(G[0]) 
    # table to store total penalties to reach at any step
    totalpen = [[0 for x in range(len(G[0]))] for x in range(len(G))]
    i = 0
    # INV2: we have our matrix filled with every row till i'th row
    # with their min penalties for every element
    while i < m:
        j = 0
        # INV1: for given ith row of matrix we get it completed till its j'th element 
        # with every element having it's lowest penalty to reach there 
        while j < n:
            # first element will be same as the original grid
            if i==0 and j==0:
                totalpen[0][0] = G[0][0]
            # to start the first row of the matrix
            elif j == 0:
                totalpen[i][0] = totalpen[i-1][0] + G[i][0]
            # to start the first column of the matrix 
            elif i == 0:
                totalpen[0][j] = totalpen[0][j-1] + G[0][j]
            # to make the rest of the matrix we will take the minimum case and 
            # add the penalty of the step to it 
            else:
                totalpen[i][j] = min(totalpen[i-1][j-1],totalpen[i-1][j],totalpen[i][j-1]) + G[i][j]
            j+=1
        i+=1
    return totalpen[m-1][n-1]

###########################################################################################################################

#2. String Problem

def stringProblem(A,B):
    m = len(A)
    n = len(B)
    vowel = ['a','e','i','o','u']
    #table for storing data of subproblems
    edit = [[0 for x in range(n + 1)] for x in range(m + 1)]
    # INV2: we have our matrix filled with every row till i'th row with their min values
    for i in range(m + 1):
        # INV1: for given ith row of matrix we get it completed till its j'th element 
        # with every element having it's lowest value
        for j in range(n + 1):
            # If first string is empty, we will insert all characters of second string
            if i == 0:
                edit[i][j] = j #it will take j steps 
            # If second string is empty, we will remove all characters of first string
            elif j == 0:
                edit[i][j] = i #it will take i steps
            # If last characters are same, we don't need to add any step 
            elif A[i-1] == B[j-1]:
                edit[i][j] = edit[i-1][j-1]
            # If last character are different, we will see every case and add a step in the min case
            # case 1 if char of A is not a vowel or characters of both A and B are vowels we have 3 cases
            elif A[i-1] not in vowel or A[i-1] in vowel and B[j-1] in vowel:
                edit[i][j] = 1 + min(edit[i][j-1],edit[i-1][j],edit[i-1][j-1])
                            #3 cases: insert^      remove^     replace^
            # case 2 if char of A is a vowel and char of B is a consonant then we have 2 cases
            # as we can not replace a vowel with a consonant
            elif A[i-1] in vowel and B[j-1] not in vowel:
                edit[i][j] = 1 + min(edit[i][j-1],edit[i-1][j])	
                            #2 cases: insert^     remove^ 
    return edit[m][n]

###############################################################################################################################

#3. Calendar Problem

# helper func to create a string of dates of a week 
def dates(l,d,r):
    s = ""
    #here i represent the days of a week with sunday as starting index 0 
    for i in range(7):
        # if the date is 1 which we have to put in string
        if d == 1:
            # if start day(l) is greater than i at the moment 
            # then we will move to next i by giving space
            if l>i:
                s = s + "   "
            #else we will add 01 to string
            else:
                if i == 6:
                    s = s + "0" + str(d)
                else:
                    s = s + "0" + str(d) + " "
                d+=1
        # for d after date of the month end(r) we will simply add empty space in the rest string
        elif d > r:
            if i == 6:
                s+="  "
            else:
                s+="   "
        # for other dates 
        else:
            if i == 6:
                #for single integer dates we add 0 in front of them
                if d//10 == 0:
                    s = s + "0" + str(d)
                else:
                    s = s + str(d)
            else:
                #for single integer dates we add 0 in front of them
                if d//10 == 0:
                    s = s + "0" + str(d) + " "
                else:
                    s = s + str(d) + " "
            d+=1
    return(s,d)

# helper func to add three strings of each month's week and 
# then arranging them to make full month
def datesline(f,l1,l2,l3,r1,r2,r3):
    d1 = 1
    d2 = 1
    d3 = 1
    # d1,d2,d3 are dates and l1,l2,l3 are index of starting day of the respective months
    # r1,r2,r3 are the month end dates respectively
    while d1 <= r1 or d2 <= r2 or d3 <= r3:
        (s1,d1) = dates(l1,d1,r1)
        (s2,d2) = dates(l2,d2,r2)
        (s3,d3) = dates(l3,d3,r3)
        # adding a line of 3 weeks of three months in order in the txt file 
        f.write("|" + s1 + " "*3+"|"+" "*3 + s2 + " "*3+"|"+" "*3 + s3 + " "*3 + "|")
        # moving to next line
        f.write("\n")
        
# Main func to make the text file of our calendar 
def printCalendar(year):
    # opening our file where we have to create calendar
    f = open("calendar.txt","w")
    # formula for finding index of 1st day of the year 
    C = (year-1)//100
    D = (year-1)%100
    l1 = (29 +D+ (D//4) +(C//4)-(2*C))%7
    # case for leap year
    if year%4 == 0:
        if year%100 != 0 or year%400 == 0:
            y = 29
    else:
        y = 28
    # string for month names 
    month = "|{0:^22} |  {1:^22}  | {2:^22}   |" 
    # string for days names 
    days = "Su Mo Tu We Th Fr Sa"
    # string for margin line
    margin = "|" + "-"*23 + "|" + "-"*26 + "|" + "-"*26 + '|'
    # we will start entering lines in our file from here
    f.write("|" + " "*23 + "|" + " "*9 + "YEAR-" + str(year) + " "*8 + "|" + " "*26 + "|")
    f.write("\n")
    f.write(margin)
    f.write("\n")
    f.write(margin)
    f.write("\n")
    f.write(month.format("<January>","<February>","<March>"))
    f.write("\n")
    f.write(margin)
    f.write("\n")
    f.write("|" + days + " "*3+"|"+" "*3  + days + " "*3+"|"+" "*3  + days + " "*3 + "|")
    f.write("\n")
    # formulae to get the starting days of next 2 months respectively
    l2 = (l1+31)%7
    l3 = (l2 + y)%7
    # code for our main month dates 
    datesline(f,l1,l2,l3,31,y,31)
    f.write(margin)
    f.write("\n")
    # now we have repeated the same procedure as above for the rest of the months 
    f.write(month.format("<April>","<May>","<June>"))
    f.write("\n")
    f.write(margin)
    f.write("\n")
    f.write("|" + days + " "*3+"|"+" "*3  + days + " "*3+"|"+" "*3  + days + " "*3 + "|")
    f.write("\n")
    l1 = (l3+31)%7
    l2 = (l1+30)%7
    l3 = (l2+31)%7
    datesline(f,l1,l2,l3,30,31,30)
    f.write(margin)
    f.write("\n")
    f.write(month.format("<July>","<August>","<September>"))
    f.write("\n")
    f.write(margin)
    f.write("\n")
    f.write("|" + days + " "*3+"|"+" "*3  + days + " "*3+"|"+" "*3  + days + " "*3 + "|")
    f.write("\n")
    l1 = (l3+30)%7
    l2 = (l1+31)%7
    l3 = (l2+31)%7
    datesline(f,l1,l2,l3,31,31,30)
    f.write(margin)
    f.write("\n")
    f.write(month.format("<October>","<November>","<December>"))
    f.write("\n")
    f.write(margin)
    f.write("\n")
    f.write("|" + days + " "*3+"|"+" "*3  + days + " "*3+"|"+" "*3  + days + " "*3 + "|")
    f.write("\n")
    l1 = (l3+30)%7
    l2 = (l1+31)%7
    l3 = (l2+30)%7
    datesline(f,l1,l2,l3,31,30,31)
    f.write(margin)
    # closing our opened file 
    f.close()

#########################################################################################################################################
