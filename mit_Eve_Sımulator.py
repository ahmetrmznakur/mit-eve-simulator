# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 20:09:10 2020

@author: ahmet akur
"""

def genTimeToSettlement(e,b):
    """
    takes two inputs e and b
    e is birthdate of mit eve
    b is the year that settled life began
    returns how many generations passed
    """
    #I assumed twenty year is the average generation time
    return (b-e)//20 
    # I used integer division because of not to take any error from loops
    # that later uses these return

def genTimeBetSettlAndIndRev(b,c):
    """
    takes two inputs b and c
    b is as indicated above the year that settled life began
    c is the year that indutrial revolution began
    returns how many generations passed between these dates
    """
    return (c-b)//20
    # I used integer division because of not to take any error from loops
    # that later uses these return

def genTimeAfterIndRev(c,d):
    """
    takes two inputs c and d
    c is the year that industrial revolution began
    as indicated above function
    d is current date
    returns how many generations passed between these dates
    """
    return (d-c)//25 #it doesnt matter 20 or 25, when we consider
                     #the shortness of this time span but it shows 
                     #I am aware of the some trends :(
    # I used integer division because of not to take any error from loops
    # that later uses these return
    


def mitocondrialEve():
    """
    takes no input but uses some user input or specified dates
    the chars in the below are those inputs or dates
    a, is initial human population
    e is the birthday of mit eve
    b is the time settled life began
    c is the time industrial revolution began
    d is the current date
    returns how many people from the initial population have descendants
    in this day(in another way how many mit eves we have)
    """
    a = int(input('how many person do you want to be in the days of mit eve: '))
    e = -int(input('how many years before the nowadays mit eve lived? '))+2020
    #because of I asked how many years before I first convert that number
#to negative and than add 2020 to find birth date
    b = -10000 #beginning of settled life
    c = 1800  #beginning of industrial revolution
    d = 2020  #current date
    import random
    initialList = list(range(1,a+1)) #first generation every number 
#indicates an ancestor
    probabilityListBeforeSettledLife = [0,0,0,1,1,1,2,2,3]
#probability set of having girl child, before settled life
#for instance probability of having one girl is 3/9 3 is number of 1s
#9 is number of whole set
    probabilityListAfterSettledLife = [0,0,1,1,2,2,2,3,3]
#probability set of having girl child, after settled life
#works as the same way with the upper set
#if you did not like the probabilities you can change that lists as you wish
    for x in range(genTimeToSettlement(e,b)):
        #print(genTimeToSettlement(e,b))#trying purposes
        newList = []
        for f in initialList:
            for g in range(random.choice(probabilityListBeforeSettledLife)):
                newList.append(f) #adds children to the list with
#expressing their ancestor number, for example all descendants of 1 expressed with 1
                #print(newList)#trying purposes
            #print(newList)#trying purposes
        initialList = newList
        #print(initialList)#trying purposes
    #print(initialList)#trying purposes
    
    for h in range(genTimeBetSettlAndIndRev(b,c)):
        #print(genTimeBetSettlAndIndRev(b,c))#trying purposes
        newList = []
        for i in initialList: #same logic applies as above
            for j in range(random.choice(probabilityListAfterSettledLife)):
                newList.append(i)
        initialList = newList
        
        
    for k in range(genTimeAfterIndRev(c,d)):
        #print(genTimeAfterIndRev(c,d))#trying purposes
        newList = []
        for l in initialList: #same logic applies as above
            for m in range(random.choice(probabilityListAfterSettledLife)):
                newList.append(l)
        initialList = newList
        
        
    differenceList = []
    for n in initialList: #a loop for finding how many different number 
#final list have and that number also equals mit eve number
        if n not in differenceList:
            differenceList.append(n)
    print(differenceList)
    print(len(differenceList))
    return len(differenceList)


def simulationNum(a):
    """
    takes one input a
    a is an integer
    runs a times the mitocondrialEve function
    and returns most likely miteve number
    and its likelihood as a tuple
    """
    ansList = []
    for num in range(a):
        ans = mitocondrialEve()
        ansList.append(ans)
    initialTuple = (0,0)
    for num1 in ansList:
        count = 0
        for num2 in ansList:
            if num1 == num2:
                count = count+1
        if count > initialTuple[1]:
            initialTuple = (num1, count)
    #if there is two or more option has the same likelihood returns the first one
    miteveNum = initialTuple[0]
    likelihood = initialTuple[1]/len(ansList)
    ansTuple =(miteveNum, likelihood)
    return ansTuple


        
        
        
   
#when you want to start the function decomment the below line and add a number in the parantheses that indicates how many times you
#want the simulation be runned  
#simulationNum()
