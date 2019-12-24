print ("Enter 5 items on shopping list")
for i in xrange(5): # range starts from 0 and ends at 5-1 (so 0, 1, 2, 3, 4 executes your loop contents 5 times)
    shopping = raw_input()
    mylist.append(shopping) # add input to the list

print (mylist) # at this point your list contains the 5 things entered by user
