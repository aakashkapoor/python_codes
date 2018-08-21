# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 17:47:33 2018

@author: Delol
"""
# Brick solving Problem

big=int(input("Enter the no of big bricks:>"))
        # To enter the number of big bricks taken
small=int(input("Enter the numbar of small bricks:>"))
        # To enter the number of small bricks taken
goal=int(input("Enter the goal of wall length you want to achieve:>"))
        # To achive the goal length of the wall
   





"""
This function is used to  make a row of bricks that achies its goal length of wall.
"""

def make_bricks(big,small,goal):
        # Defination used to create the wall from various inputs/paramerters passes
    if (big*5) + small == goal:
            # Condition to check when big bricks are *5 and small bricks are added 
        return True
            # If goal is achieved then return true
    elif (goal//5) >= goal:
            # Else the remainder of goal is calculated
        return True
            # If it satisfies the value then return True
    elif small >= goal:
            # Else if the the no of small bricks are greater thyan or equal to the goal to be achieved.
        return True
            # If it satisfies the value then return True
    else:
        #If above conditions don't validate then:
        bn = goal//5
        # Bn=new variable for big bricks which stores the result of remainder in bn.
        sn = goal - (bn*5)
            # Sn=new variable for small bricks which stores the result when diffrence between (goal - (bn*5))
        if big>= bn and sn<=small:
            # If statement used when big is greater than or equal to bn likeways for sn
            return True
                #If it satisfies the value then return True 
        elif big < bn and goal<= (big*5) + small:
            #If statement used when big is less than bn and goal is less than ((big*5) + small)
            return True
            #If it satisfies the value then return True 
        else:
            #If above conditions don't validate then:
            return False
               #If it doesn't satisfies the value then return True  
               
   



            
               
              
make_bricks(big,small,goal)
        # Function called for execution