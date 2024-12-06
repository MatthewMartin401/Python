#Vending Machine

option= None
o_list = {1:"soda" , 2:"chocolate" , 3:"crisps"}

leave=False
while leave == False:
#Try user input and find whether its valid.
    try:
        error=False
        option=int(input(f"Pick one from list {o_list} or input 0 to Leave:"))

    except (ValueError):
        print("Error")
        error=True

        
#Try inputting the selected option
    try:        #As finally cannot be used, as it doesnt support an additional except. This means a second try has to be used.
        if error != True:
            if option == 0:
                print("you have left")
                leave = True
            else:
                print ("you have chosen: "+o_list[option])
    except KeyError:
        print("Option not Valid")
        error=True

    finally:
        if error != True: #Has to be included, as an ValueError or KeyError can cause an Error. As finally doesnt support except, an if condition has to be used.
            print (o_list[option]+ " has been distributed.")
    
