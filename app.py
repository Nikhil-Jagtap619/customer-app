# creating a dictionary
recharge = {1:{1:["45 rs = 1GB/day",45],
               2:["159 rs = 2GB for 25days",159],
               3:["231 rs = 1GB/day for 25days",231]},
            2:{1:["20 rs = 20 TT",20],
               2:["99 rs = unl TT & unl SMS for 3days",99],
               3:["159 rs = Unl TT & SMS for 25days",159]}}

def number():  # a fucntion to get user's number
    numb = True
    num = None
    while numb: # a loop to get the number of exact 10 digits
        num = input("Enter your phone number: ")
        if len(num) == 10:
            num = int(num)
            numb = False
        else:
            print("Retry! number isn't 10 digits")
            continue
    return num

customer = dict() # to save customer details
amt = 0
print("Welcome to Airtel Recharge app \n")
app = True
while app:
    print("make your choice using a number: ")
    user = int(input("1: Current Balance\n2: Recharge : "))
    if user==2:
        choice = int(input("1: Internet\n2: Talktime & SMS : "))
        if choice in recharge:
            for k,v in recharge[choice].items():

                print(f"{k}: {v[0]}")  #prints all the available offers
            use = int(input("What pack would you prefer? : "))
            if use in recharge[choice]:
                amt += recharge[choice][use][1] # adds the amount 
                cell_num = number()
                if cell_num not in customer:   # if a customer is new creates new record as save
                    customer[cell_num] = list()
                    customer[cell_num].append(recharge[choice][use][0])
                else:
                    customer[cell_num].append(recharge[choice][use][0])
                print("Redirecting to UPI......")
                print(f"your number {cell_num} has been recharged with {recharge[choice][use][0]}, amount = {float(amt)} \n")
                print("▁ ▂ ▄ ▅ ▆ ▇ █ Recharge Complete █ ▇ ▆ ▅ ▄ ▂ ▁")
            else:
                print('''
                ███████▄▄███████████▄
                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                ▓▓▓▓▓▓███░░░░░░░░░░░░█
                ██████▀░░█░░░░██████▀
                ░░░░░░░░░█░░░░█
                ░░░░░░░░░░█░░░█
                ░░░░░░░░░░░█░░█
                ░░░░░░░░░░░█░░█
                ░░░░░░░░░░░░▀▀
                \n you idiot? use number''')
        else:
            print('''
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░▄▄▄▄▄▄▄░░░░░░░░░
            ░░░░░░░░░▄▀▀▀░░░░░░░▀▄░░░░░░░
            ░░░░░░░▄▀░░░░░░░░░░░░▀▄░░░░░░
            ░░░░░░▄▀░░░░░░░░░░▄▀▀▄▀▄░░░░░
            ░░░░▄▀░░░░░░░░░░▄▀░░██▄▀▄░░░░
            ░░░▄▀░░▄▀▀▀▄░░░░█░░░▀▀░█▀▄░░░
            ░░░█░░█▄▄░░░█░░░▀▄░░░░░▐░█░░░
            ░░▐▌░░█▀▀░░▄▀░░░░░▀▄▄▄▄▀░░█░░
            ░░▐▌░░█░░░▄▀░░░░░░░░░░░░░░█░░
            ░░▐▌░░░▀▀▀░░░░░░░░░░░░░░░░▐▌░
            ░░▐▌░░░░░░░░░░░░░░░▄░░░░░░▐▌░
            ░░▐▌░░░░░░░░░▄░░░░░█░░░░░░▐▌░
            ░░░█░░░░░░░░░▀█▄░░▄█░░░░░░▐▌░
            ░░░▐▌░░░░░░░░░░▀▀▀▀░░░░░░░▐▌░
            ░░░░█░░░░░░░░░░░░░░░░░░░░░█░░
            ░░░░▐▌▀▄░░░░░░░░░░░░░░░░░▐▌░░
            ░░░░░█░░▀░░░░░░░░░░░░░░░░▀░░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n what you doing? use numbers!''')
    else:
        cell_num = number()
        print(f"number : {cell_num} \n your current balance is {float(amt)}")

    ans = input("get back to menu? [Y/N] ")
    if ans.lower() != "y":
        app = False

print(f"customer details so far: {customer}")




