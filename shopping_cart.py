# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 18:47:14 2018

@author: Delol
"""

shopping_list = []
#Here we create a list of shopping items
print ( "What should we pick up at the store ? ")  
        # User inputs the items that he/she wishes to have.
print ( "Enter ‘DONE’ to stop adding items. ")
#DONE for the termination of program and displaying all the items in your list


"""
This function is preapred to accept comma separated values from the user.
This also provides convinence to the user to add multiple items to the shopping list rather by entering one by one. 
"""
def comma_sep(new_item):      
          # To enter items separated by comma.
    for pack in new_item.split(','):   
            #split operation helps to split comma separated input.
        if(len(pack)==0):      
               # for calculating the length.
            continue
        shopping_list.append(pack)  
               # To append/add the items in the shopping list.


#end of entering comma separated function

"""
This Function is used to add values in the shopping list and append each values and update the list.
"""
def add_to_list(new_item):     
        # To enter items in the list.
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list))) 
          # to display each value inputed in the list
    

#end of add to list function

"""
This function helps the user to enter the item at a specific index as defined by the user criteria
"""   
def add_at_index(new_item):    
    a=int(input("Enter the index where you want to add your item:>"))
    insert_at=a
    insert_items=raw_input("Enter the item you want to insert:>")
    shopping_list.insert(insert_at,insert_items)   
         # Syntax for inserting items at a particular location.
    print " Final List:",shopping_list      
          # Printing the final Updated List.

#end of addition function

"""
This Function is made to delete a paricular item either by name or by index value.
This function also provides the user to re-enter the name or index again in case of wrong input.
"""
def del_at_index(new_item):    
           #For deletion of an element at a particular index or by name.
    while True:
        try:                  
                 # try-catch block for helping the user to give correct values and names.
            delete_item=raw_input("Enter the index or name where you want to delete your item:>")
            if delete_item.isdigit():   
                      # If user wants to delete items by index location.
                shopping_list.pop(delete_item)
                print " Final List:",shopping_list
            else:
                shopping_list.remove(delete_item)  
                     # If user wants to delete items by entering the item name.
                print " Final List:",shopping_list
            break
        except:      
               # if not valid input is provided the user is given chance to correct that particular entry.
                print("Enter the name or the index value of the item again")

#end of delete function



while True:     
        # Main code starts till will loop will not get over.
    print ("1. Enter your Items either comma separated or single item to add in shopping list")
    print ("2. Enter 1 for adding items to a Specific Index")
    print ("3. Enter 2 to Delete an Item from Specific Index")
    new_item = raw_input(" Item name > ")   
        # For inputing the items that user wants.
    
    
    if new_item.upper() == 'HELP':   
               # Shows the help case operation available at any point of time.
        print ("SHOW :- It gives you the view of your shopping list at any intermediate steps")
        print ("DONE :- It helps the user to checkout when one has collected all the required items ; And displays the end list of items in your cart")
        continue    
             # This statement is called so as the program does not terminate and continues for user input.
    
    
    if new_item.upper() == 'SHOW':   
              #To show all the items entered by user without terminating the program at any point.
        for item in shopping_list:
            print ( item )
        continue        
              # This statement is called so as the program does not terminate and continues for user input.
    
    
    if new_item.upper() == 'DONE':   
              # This means that the user has all the items in the list needs to checkout.
        print (shopping_list)     
              # Final shopping list is displayed.
        break     
            # To break and end the loop
    
    
    if new_item.isdigit():
        #choice=int(input("Enter the choice of operation you like to select:>"))
        if new_item == "1":    
            # Called for adding at a specific index.
            add_at_index(new_item)
            
        elif new_item == "2":    
            # called for deleting the items wrongly input in the list.
            del_at_index(new_item.isalpha)
        
        else:             
            # If the user enter any other values rather than 1,2.
            print ("Please Enter the correct choice of operation")
        
    else:         
        # For simple input and comma separated input provided by user.
        comma_sep(new_item)
        continue      
             # This statement is called so as the program does not terminate and continues for user input.



    