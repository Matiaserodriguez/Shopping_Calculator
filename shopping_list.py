products = []
prices = []
options = ['Add item', 'View Cart', 'Remove Item', 'Compute total', 'Quit']

new_item = ''
action = ''

wants_shopping = True

print('Welcome to the Shopping Cart Program!')

while action != '5':
    wants_shopping = True
    remove_item = None

    print('\nWhat do you want to do?')
    for i in range(len(options)):
        choices = options[i]
        print(f'{i + 1}. {choices}')

    action = input('Please enter an action: ')

    if action == '1':
        new_item = ''
        while new_item == '':
            new_item = input('What product would you like to add? ')
            new_price = ''
            while new_price == '':
                try:
                    new_price = float(input(f'What is the price of the {new_item}? $'))
                except ValueError:
                    print('Please, type a number. Instead of comma use point.')
                    continue

            products.append(new_item)
            prices.append(new_price)
            print(f'{new_item.title()} has been added to the cart.')

    elif action == '2':
        if products == []:
            print('You don\'t have any items in the cart.')
        elif products != []:
            print('The products of the cart are: ')
            for i in range(len(products)):
                print(f'{i + 1}. {products[i].title()} - ${prices[i]:.2f}')
    
    elif action == '3':
        if products == []:
            print('You don\'t have any items to remove')
        elif products != []:
            remove_item = ''
            while remove_item == '':
                try:
                    remove_item = int(input('What item do you gonna remove? '))
                except ValueError:
                    print('Please, type a number from index and not a product.')
                    continue
            while remove_item not in range(0, len(products) + 1):
                remove_item = int(input('What item do you gonna remove? '))
            products.pop(remove_item - 1)
            prices.pop(remove_item - 1)
            print(f'Product {remove_item} has been removed')

    
    elif action == '4':
        compute = sum(prices)
        print(f'The total amount is: ${compute:.2f}')
    
    elif action == '5':
        wants_shopping = False
        print('Thank you, good bye.')
    
    else:
        print('Invalid input, please try again')