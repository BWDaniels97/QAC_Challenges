
'''

Challenge of the day 2

Create a times table square!

'''

def multiply_grid():

    n = int(input("Enter number: "))

    for x in range (1, n+1):
        for y in range (1, n+1):
            print (x*y,'\t',end=" ")
        print('\n')
    again()


def again():

    again_choice = input('Do you want play again (Y)es or (N)o:')
    if again_choice.upper() == 'Y':
        multiply_grid()
    elif again_choice.upper() == 'N':
        print('Goodbye!')
    else:
        print('Invalid choice!')
        again()

        
multiply_grid()