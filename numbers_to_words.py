

number = { 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',\
     7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',\
          13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', \
                17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}


number2 = ['', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

hundred = 'hundred'

thousand = 'thousand'



num = int(input('Enter number:'))



if num < 20:
    print(number[num])

elif num < 100:

    num = (divmod(num, 10))

    if num[1] == 0:
        print(number2[num[0]])



    elif num[1] != 0:
        

        print(number2[num[0]], number[num[1]])


elif num >= 100 and num < 1000:

    list1 = list(str(num))

    if list1[2] == '0' and list1[1] == '0':

        print(number[int(list1[0])], hundred)


    elif list1[2] == '0' and list1[1] != '0':

        print(number[int(list1[0])], hundred, 'and', number2[int(list1[1])])

    elif list1[2] != '0' and list1[1] == '0':

        print(number[int(list1[0])], hundred, 'and', number[int(list1[2])])

    elif list1[2] != '0' and list1[1] != '0':

        print(number[int(list1[0])], hundred, 'and', number2[int(list1[1])], number[int(list1[2])])



elif num >= 1000:

    list1 = list(str(num))

    if list1[1] == '0' and list1[2] == '0' and list1[3] == '0':

        print(number[int(list1[0])], thousand)


    elif list1[1] != '0' and list1[2] == '0' and list1[3] == '0':

        print(number[int(list1[0])], thousand, number[int(list1[1])], hundred)
    
    elif list1[1] != '0' and list1[2] != '0' and list1[3] == '0':

        print(number[int(list1[0])], thousand, number[int(list1[1])], hundred, 'and', number2[int(list1[2])])
    
    elif list1[1] != '0' and list1[2] != '0' and list1[3] != '0':

        print(number[int(list1[0])], thousand, number[int(list1[1])], hundred, 'and', number2[int(list1[2])], number[int(list1[3])])
    
    elif list1[1] == '0' and list1[2] == '0' and list1[3] != '0':

        print(number[int(list1[0])], thousand, 'and', number[int(list1[3])])
    
    elif list1[1] == '0' and list1[2] != '0' and list1[3] != '0':

        print(number[int(list1[0])], thousand, 'and', number2[int(list1[2])], number[int(list1[3])])

    else: 

        print(number[int(list1[0])], thousand, number[int(list1[1])], hundred, 'and', number[int(list1[3])])

        
