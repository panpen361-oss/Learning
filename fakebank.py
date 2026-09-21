"""
username = input("Enter a username: ")

if len(username) > 12:
    print("Your username cant be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username cant contain spaces")
elif not username.isalpha():
    print("Your username cant contain numbers")
else:
    print(f"Welcome {username}")


--------------------------------------

print('1. Borrow loan')
print('2. Investment future calc')
print('3. International Transfer')
print('4. ')
choice = int(input('Enter your choice: '))
"""



user_username = 'Phan Nguyen'
user_password = 'Chaseaccount'
qualify_user = True 
user_balance = 30000

print('Welcome to Chase Bank')
user_status = int(input('Type 1 to sign up, Type 2 to sign in.: '))

if user_status == 2:
    check_name = input('Enter your username: ')
    check_pass = input('Enter your password: ')
if check_name == user_username and check_pass == user_password:
    user_verify = True
    print('Succesfully sign in')

else:
    print('Username or password is inccorrect')

if user_verify == True:
    print('\n1. Borrow loan, \n2. Investment future calc, \n3. International Transfer, \n4. Subscription list')
    choice_finance = int(input('Enter your choice: '))


    rate_reduce = 0.2
    
    package1_percent = 4
    package2_percent = 2.5
    package3_percent = 1.5
    package4_percent = 1
    package5_percent = 0.5
    
    package1 = 3000
    package2 = 12500
    package3 = 50000
    package4 = 250000
    package5 = 1000000
    
    payoff_months = 24


if choice_finance == 1:
    print(f'Welcome to our Loaning system, take a look at our package we offer.')
    print(f'1. ${package1:,}, Monthly rate interest: {package1_percent}%')
    print(f'2. ${package2:,}, Monthly rate interest: {package2_percent}%')
    print(f'3. ${package3:,}, Monthly rate interest: {package3_percent}%')
    print(f'4. ${package4:,}, Monthly rate interest: {package4_percent}%')
    print(f'5. ${package5:,}, Monthly rate interest: {package5_percent}%')
    package_choice = int(input('Choose which package you like: '))

if package_choice == 1 and (qualify_user or user_balance >= 20000):
    
    print(f'You qualify for less interest rate on package 1 instead of {package1_percent}%')
    package1_newrate = package1_percent - rate_reduce
    
    print(f'Package 1 new rate is now: {package1_newrate}%')

    package1_interest = package1 * (package1_newrate / 100)
    package1_total = package1 + package1_interest
    monthly_pay = package1_total / payoff_months
    print('Loan recipe')
    print('Package 1')
    print(f'amount: ${package1:,}')
    print(f'Pay off in {payoff_months} months')
    print(f'Total amount(Fees apply): ${package1_total:,.2f}')
    print(f'Each month pay: ${monthly_pay:2f}')
    
    package_deal = input('Type yes to agree on the loan deal, type no to cancel: ')
    if package_deal == 'yes':
        print('Thank you for loaning from us!')
    elif package_deal == 'no':
        print('If our deal not what you look for, we will try our best to offer you the best deal next time!')
    else:
        print('Error, please type yes or no only.')

elif package_choice == 1:
    package1_interest = package1 * (package1_percent / 100)
    package1_total = package1 + package1_interest
    monthly_pay = package1_total / payoff_months
    print(f'package 1 value: ${package1:,.2f} \nRate: {package1_percent}% \nPay in {payoff_months} months, each month will pay: ${monthly_pay:,.2f} \nTotal payback: ${package1_total:,.2f}')

    package_deal = input('Type yes to agree on the loan deal, type no to cancel: ')
    if package_deal == 'yes':
        print('Thank you for loaning from us!')
    elif package_deal == 'no':
        print('If our deal not what you look for, we will try our best to offer you the best deal next time!')
    else:
        print('Error, please type yes or no only.')

# ------------------------------

elif package_choice == 2 and (qualify_user or user_balance >= 100000):
    
    print(f'You qualify for less interest rate on package 2 instead of {package2_percent}%')
    package2_newrate = package2_percent - rate_reduce
    
    print(f'Package 2 new rate is now: {package2_newrate}%')

    package2_interest = package2 * (package2_newrate / 100)
    package2_total = package2 + package2_interest
    monthly_pay = package2_total / payoff_months
    print('Loan recipe')
    print('Package 2')
    print(f'amount: ${package2:,}')
    print(f'Pay off in {payoff_months} months')
    print(f'Total amount(Fees apply): ${package2_total:,.2f}')
    print(f'Each month pay: ${monthly_pay:.2f}')
    
    package_deal = input('Type yes to agree on the loan deal, type no to cancel: ')
    if package_deal == 'yes':
        print('Thank you for loaning from us!')
    elif package_deal == 'no':
        print('If our deal not what you look for, we will try our best to offer you the best deal next time!')
    else:
        print('Error, please type yes or no only.')

elif package_choice == 2:
    package2_interest = package2 * (package2_percent / 100)
    package2_total = package2 + package2_interest
    monthly_pay = package2_total / payoff_months
    print(f'package 2 value: ${package2:,.2f} \nRate: {package2_percent}% \nPay in {payoff_months} months, each month will pay: ${monthly_pay:,.2f} \nTotal payback: ${package2_total:,.2f}')

    package_deal = input('Type yes to agree on the loan deal, type no to cancel: ')
    if package_deal == 'yes':
        print('Thank you for loaning from us!')
    elif package_deal == 'no':
        print('If our deal not what you look for, we will try our best to offer you the best deal next time!')
    else:
        print('Error, please type yes or no only.')

#------------------------------

# ------------------------------

elif package_choice == 3 and (qualify_user or user_balance >= 350000):
    
    print(f'You qualify for less interest rate on package 3 instead of {package3_percent}%')
    package3_newrate = package3_percent - rate_reduce
    
    print(f'Package 3 new rate is now: {package3_newrate}%')

    package3_interest = package3 * (package3_newrate / 100)
    package3_total = package3 + package3_interest
    monthly_pay = package3_total / payoff_months
    print('Loan recipe')
    print('Package 3')
    print(f'amount: ${package3:,}')
    print(f'Pay off in {payoff_months} months')
    print(f'Total amount(Fees apply): ${package3_total:,.2f}')
    print(f'Each month pay: ${monthly_pay:.2f}')
    
    package_deal = input('Type yes to agree on the loan deal, type no to cancel: ')
    if package_deal == 'yes':
        print('Thank you for loaning from us!')
    elif package_deal == 'no':
        print('If our deal not what you look for, we will try our best to offer you the best deal next time!')
    else:
        print('Error, please type yes or no only.')

elif package_choice == 3:
    package3_interest = package3 * (package3_percent / 100)
    package3_total = package3 + package3_interest
    monthly_pay = package3_total / payoff_months
    print(f'package 3 value: ${package3:,.2f} \nRate: {package3_percent}% \nPay in {payoff_months} months, each month will pay: ${monthly_pay:,.2f} \nTotal payback: ${package3_total:,.2f}')

    package_deal = input('Type yes to agree on the loan deal, type no to cancel: ')
    if package_deal == 'yes':
        print('Thank you for loaning from us!')
    elif package_deal == 'no':
        print('If our deal not what you look for, we will try our best to offer you the best deal next time!')
    else:
        print('Error, please type yes or no only.')

#------------------------------
# ------------------------------

elif package_choice == 4 and (qualify_user or user_balance >= 750000):
    
    print(f'You qualify for less interest rate on package 4 instead of {package4_percent}%')
    package4_newrate = package4_percent - rate_reduce
    
    print(f'Package 4 new rate is now: {package4_newrate}%')

    package4_interest = package4 * (package4_newrate / 100)
    package4_total = package4 + package4_interest
    monthly_pay = package4_total / payoff_months
    print('Loan recipe')
    print('Package 4')
    print(f'amount: ${package4:,}')
    print(f'Pay off in {payoff_months} months')
    print(f'Total amount(Fees apply): ${package4_total:,.2f}')
    print(f'Each month pay: ${monthly_pay:.2f}')
    
    package_deal = input('Type yes to agree on the loan deal, type no to cancel: ')
    if package_deal == 'yes':
        print('Thank you for loaning from us!')
    elif package_deal == 'no':
        print('If our deal not what you look for, we will try our best to offer you the best deal next time!')
    else:
        print('Error, please type yes or no only.')

elif package_choice == 4:
    package4_interest = package4 * (package4_percent / 100)
    package4_total = package4 + package4_interest
    monthly_pay = package4_total / payoff_months
    print(f'package 4 value: ${package4:,.2f} \nRate: {package4_percent}% \nPay in {payoff_months} months, each month will pay: ${monthly_pay:,.2f} \nTotal payback: ${package4_total:,.2f}')

    package_deal = input('Type yes to agree on the loan deal, type no to cancel: ')
    if package_deal == 'yes':
        print('Thank you for loaning from us!')
    elif package_deal == 'no':
        print('If our deal not what you look for, we will try our best to offer you the best deal next time!')
    else:
        print('Error, please type yes or no only.')

#------------------------------
# ------------------------------

elif package_choice == 5 and (qualify_user or user_balance >= 1000000):
    
    print(f'You qualify for less interest rate on package 5 instead of {package5_percent}%')
    package5_newrate = package5_percent - rate_reduce
    
    print(f'Package 5 new rate is now: {package5_newrate}%')

    package5_interest = package5 * (package5_newrate / 100)
    package5_total = package5 + package5_interest
    monthly_pay = package5_total / payoff_months
    print('Loan recipe')
    print('Package 5')
    print(f'amount: ${package5:,}')
    print(f'Pay off in {payoff_months} months')
    print(f'Total amount(Fees apply): ${package5_total:,.2f}')
    print(f'Each month pay: ${monthly_pay:.2f}')
    
    package_deal = input('Type yes to agree on the loan deal, type no to cancel: ')
    if package_deal == 'yes':
        print('Thank you for loaning from us!')
    elif package_deal == 'no':
        print('If our deal not what you look for, we will try our best to offer you the best deal next time!')
    else:
        print('Error, please type yes or no only.')

elif package_choice == 5:
    package5_interest = package5 * (package5_percent / 100)
    package5_total = package5 + package5_interest
    monthly_pay = package5_total / payoff_months
    print(f'package 5 value: ${package5:,.2f} \nRate: {package5_percent}% \nPay in {payoff_months} months, each month will pay: ${monthly_pay:,.2f} \nTotal payback: ${package5_total:,.2f}')

    package_deal = input('Type yes to agree on the loan deal, type no to cancel: ')
    if package_deal == 'yes':
        print('Thank you for loaning from us!')
    elif package_deal == 'no':
        print('If our deal not what you look for, we will try our best to offer you the best deal next time!')
    else:
        print('Error, please type yes or no only.')
        

#------------------------------
 
   
elif choice_finance == 2:
    print('1. House Flipping')
    print('2. Bank annual return')
    print('3. Stock')
    investment_choice = int(input('Choose your investment plan'))

    if investment_choice == 1:
        capitals_fund = 3000000
        print('House Flipping')
        print(f'Total capitals of ${capitals_fund:,.2f}')
        print('House option: ')
        house1_price = 450000
        house2_price = 885000
        house3_price = 1450000
        print(f'1.3 bedroom, 2 bathroom, no backyard, 1,000 square feet, cost ${house1_price}')
        print(f'1.4 bedroom, 2 bathroom, have backyard, 1,887 square feet, cost ${house2_price}')
        print(f'1.5 bedroom, 3 bathroom, have backyard, 3,139 square feet, have pool, cost ${house3_price}')
        house_option = int(input('Select which house you want to calculate the profit you earn per month'))
        if house_option == 1:
            print('')
        elif house_option == 2:
            print('')
        elif house_option == 3:
            print('')
        else:
            print('Sorry your input is not valid! please choose 1-3 since those the only thing we got to offer.')
    elif investment_choice == 2:
        print('')
    elif investment_choice == 3:
        print('')


elif choice_finance == 3:
    print('')
elif choice_finance == 4:
    print('')
else:
    print('Invalid choice')
