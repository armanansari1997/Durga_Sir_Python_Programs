if __name__ == '__main__':
    l1 = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
    print(l1[0])  # (10, 20, 30)
    print(l1[0][1])  # 20
    print(l1[1])  # (40, 50, 60)
    print(l1[1][2])  # 60

    # eg-2
    d = {
        'cars': ('Innova', 'Honda', 'Maruti'),
        'mobiles': ('Samsung', 'Iphone', 'Nokia')
    }

    # To display 2nd car name
    print(d['cars'][1])  # Honda
    print(d.get('cars')[1])  # Honda

    # To display all mobile names
    print(d['mobiles'])  # ('Samsung', 'Iphone', 'Nokia')
    print(d.get('mobiles'))  # ('Samsung', 'Iphone', 'Nokia')
    for mobile in d['mobiles']:
        print(mobile)

    supermarket = {
        'store1': {
            'name': 'Durga General Store',
            'items': [
                {'name': 'soap', 'quantity': 20},
                {'name': 'brush', 'quantity': 30},
                {'name': 'pen', 'quantity': 40}
            ]
        },
        'store2': {
            'name': 'Sunny Book Store',
            'items': [
                {'name': 'python', 'quantity': 100},
                {'name': 'django', 'quantity': 200},
                {'name': 'java', 'quantity': 300}
            ]
        }
    }

    # To print name of store1
    print(supermarket['store1']['name']) # Durga General Store
    print(supermarket.get('store1').get('name')) # Durga General Store

    # To display name of all items present in store1
    items = supermarket.get('store1').get('items')
    print(items) # [{'name': 'soap', 'quantity': 20}, {'name': 'brush', 'quantity': 30}, {'name': 'pen', 'quantity': 40}]
    for item in items:
        print(item.get('name'))
        # print(item['name'])
    # soap
    # brush
    # pen

    # To display quantity of django item present in store2
    items = supermarket.get('store2').get('items')
    print(items) # [{'name': 'python', 'quantity': 100}, {'name': 'django', 'quantity': 200}, {'name': 'java', 'quantity': 300}]
    for item in items:
        if item['name'] == 'django':
            print(item['quantity']) # 200
            # print(item.get('quantity')) # 200