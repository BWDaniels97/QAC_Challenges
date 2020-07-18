
'''

Challenge of the day 2

Create a times table square!

'''

def multiply_grid(x):

    mylist = []
    
    

    for a in range (1, x+1):
        
        for b in range (1, x+1):
            
            mylist.append(a*b)
            mylist.append('\t')
        
        mylist.append('\n')
            
           
    return mylist
    
    
    



        
    
n = int(input("Enter number: "))

print(*multiply_grid(n))